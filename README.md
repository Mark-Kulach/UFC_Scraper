#### Data Scraper
- Part of unfinished AI MMA Coach Project

### PLAN
- Scrape footage / stats from internet, store in postgres db
    - Chose UFC Footage instead of personal footage so model would be trained on high level athletes (Important when converting into a coach ig)
    - The idea is to teach model to recognize patterns on its own instead of hardcoding specific rules of fighting
    - For grappling pose data will be inaccurate, but it might be consistently innacurate in a way where you can still recognize scenario
- Scrape footage / stats from internet, store in postgres db
    - Store data in a way where you see correlations between many different datapoints
        - Their build, their favorite techniques, their weaknesses, their skill development, favorable matchups
- Train model to accurately convert new footage into usable data  
    - Use public stats data as benchmark for performance during training
    - Further break down each datapoint into it's specific technique by manually labelling footage (Manual work will be sped up significantly once footage is categorized)
    - Train model to pick up on patterns in differences between landed / missed techniqes (No idea)
    - Train model to start ranking the effectiveness of a technique, pointing out mistakes, and pointing out improvements (no idea)
- Use ChatGPT API to answer user questions (chatGPT should be able to pull general advice from internet, just need)
- Build a frontend IOS app where user can upload their own footage and get direct feedback