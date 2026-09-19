import os
import requests
import time

def filter_tenders(tenders, keywords):
    api_key = os.environ.get('GROQ_API_KEY')
    if not api_key:
        print("GROQ_API_KEY missing!")
        return []

    print(f"API Key length: {len(api_key)}")
    print(f"API Key starts with: {api_key[:10]}...")

    matches = []
    for t in tenders:
        prompt = f"""Tender title: {t['title']}
User is looking for: {keywords}

Kya yeh tender in keywords se related hai? Sirf YES ya NO likho."""

        try:
            r = requests.post(
                'https://api.groq.com/openai/v1/chat/completions',
                headers={
                    'Authorization': f'Bearer {api_key}',
                    'Content-Type': 'application/json'
                },
                json={
                    'model': 'openai/gpt-oss-120b',
                    'messages': [{'role': 'user', 'content': prompt}],
                    'temperature': 0
                },
                timeout=30
            )
            
            print(f"Response status: {r.status_code}")
            
            data = r.json()
            
            if 'choices' in data:
                answer = data['choices'][0]['message']['content'].strip()
                print(f"AI answer: {answer}")
                if 'YES' in answer.upper():
                    matches.append(t)
                    print(f"✅ Match: {t['title']}")
                else:
                    print(f"❌ No match: {t['title']}")
            else:
                print(f"Unexpected response: {data}")
                
        except Exception as e:
            print(f"AI error: {e}")
        
        # Rate limit se bachne ke liye 2 second wait
        time.sleep(2)

    return matches
