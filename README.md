# GNote

**GNote** is a lightning-fast terminal tool for taking daily work notes and generating AI-powered summaries.

---

### 🚀 Example Usage

note                      # Opens today's note in Notepad  
note Fixed Docker issue   # Appends "Fixed Docker issue" to today's note (quotes are optional)  
notesum --last Xd         # Summarizes your notes from the last X days (requires OpenAI API key)

---

### ⚙️ Installation & Setup

1. **Clone this repository**

   git clone https://github.com/yourusername/GNote.git

2. **Navigate to the project directory**

   cd GNote

3. **Create a `.env` file**
   - Use `.env.example` as a reference.
   - Specify where you want GNote to store your notes.

4. **Set your OpenAI API key (in PowerShell as Administrator)**

   setx OPENAI_API_KEY "sk-your-api-key-here"

5. **Install via pipx**

   pipx install .

6. **Restart your terminal**  
   You're ready to start using **GNote**!

---

💡 **Tip:** Run `note` anytime to open or append to your daily note, and `notesum` to get quick summaries powered by AI.
