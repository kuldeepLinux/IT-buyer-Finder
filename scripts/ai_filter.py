import os
import requests

def filter_tenders(tenders, keywords):
    api_key = os.environ.get('GROQ_API_KEY')
    if not api_key:
        print("GROQ_API_KEY missing!")
        return []

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
                    'model': 'llama-3.1-8b-instant',
                    'messages': [{'role': 'user', 'content': prompt}],
                    'temperature': 0
                },
                timeout=30
            )
            answer = r.json()['choices'][0]['message']['content'].strip()
            if 'YES' in answer.upper():
                matches.append(t)
                print(f"Match: {t['title']}")
        except Exception as e:
            print(f"AI error: {e}")

    return matches
