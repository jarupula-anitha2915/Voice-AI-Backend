Voice AI Backend serves chunked, relevant info under 800 tokens for Retell AI agents, maintains conversation context, and logs interactions to Google Sheets. Built with FastAPI and SentenceTransformers, it's optimized for real-time performance and accurate response delivery.
✅ 1. What was your initial thought process when you first read the problem statement, and how did you break it down into smaller, manageable parts?
When I first read the problem, it seemed a bit overwhelming because there were many things to implement — APIs, chunking information, context management, and even logging into Google Sheets. So, I broke it down into smaller steps to stay organized.

I split it into these parts:

First, set up a basic FastAPI project

Then, build the core API that returns responses (with the 800-token limit in mind)

Next, add routing logic to serve relevant information

After that, implement a way to track conversation context

Finally, connect the app to Google Sheets to log conversation data automatically

This approach helped me work on one part at a time without feeling lost.

✅ 2. What specific tools, libraries, or online resources did you use to develop your solution, and why did you choose them over other options?
I used these main tools/libraries:

FastAPI: For creating the APIs because it's lightweight, fast, and easy to use.

SentenceTransformers: To find relevant chunks based on user queries using semantic similarity.

gspread + Google Sheets API: To log conversations in a simple and visual way.

Python’s standard libraries: For time, file handling, and basic utilities.

I also referred to Retell AI documentation for understanding integration constraints, and Stack Overflow + GitHub issues whenever I was stuck. These tools were chosen for their simplicity, documentation support, and easy integration with the project.

✅ 3. Describe a key challenge you faced while solving this problem and how you arrived at the final solution?
One of the biggest challenges I faced was with the Google Sheets integration. At first, I didn’t know how to set up the credentials, and the API seemed a bit confusing. Also, it was asking me to pay for some Google Cloud services, which was unexpected.

To solve this, I carefully followed step-by-step instructions from the gspread documentation and tutorials online. I also learned how to create a service account properly and share the sheet with the right email address found in the google_creds.json file.

Another issue was with the sentence-transformers library throwing errors — I fixed it by downgrading the transformers version to one that works well with it.

✅ 4. If you had more time, what improvements or alternative approaches would you explore, and why do you think they might be valuable?
If I had more time, I would:

Use a real database (like MongoDB or PostgreSQL) to store chat history instead of Google Sheets for better scalability and query flexibility.

Add authentication and rate-limiting to the API to make it more secure.

Implement context memory using Redis so the bot can remember things over longer conversations.

Use streaming chunk responses for smoother voice AI experiences.

These changes would help make the system more robust, scalable, and suitable for real-world production use.
