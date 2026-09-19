def scrape_cpwd():
    """
    Demo data - CPWD block kar raha hai (403 Forbidden)
    Baad mein real source add karenge
    """
    print("Demo tenders load kar rahe hain...")
    
    tenders = [
        {
            'nit': 'CPWD/2026/001',
            'title': 'Firewall Installation for Faridabad Data Center',
            'cost': '₹15,00,000',
            'deadline': '25 Oct 2026'
        },
        {
            'nit': 'CPWD/2026/002',
            'title': 'Laptop Supply for Haryana Government Office',
            'cost': '₹8,50,000',
            'deadline': '28 Oct 2026'
        },
        {
            'nit': 'CPWD/2026/003',
            'title': 'Server Rack Supply for Delhi IT Department',
            'cost': '₹22,00,000',
            'deadline': '30 Oct 2026'
        },
        {
            'nit': 'CPWD/2026/004',
            'title': 'Office Furniture Supply',
            'cost': '₹5,00,000',
            'deadline': '1 Nov 2026'
        }
    ]
    
    print(f"Total tenders: {len(tenders)}")
    return tenders
