# GNote

**GNote** is a lightning-fast terminal tool for taking daily work notes and generating AI-powered summaries.

---

### 🚀 Example Usage
```bash
note                         # Opens today's note in Notepad  
note "Fixed Docker issue"    # Appends "Fixed Docker issue" to today's note (quotes are optional)  
notesum --last Xd            # Summarizes your notes from the last X days (requires OpenAI API key)

...more commands on the way
```
---

### ⚙️ Installation & Setup

1. **Clone this repository**
```bash
   git clone https://github.com/yourusername/GNote.git
```
2. **Navigate to the project directory**
```bash
   cd GNote
```
3. **Create a `.env` file**
   - Use `.env.example` as a reference.
   - Specify where you want GNote to store your notes.

5. **Set your OpenAI API key (in PowerShell as Administrator)**
```bash
   setx OPENAI_API_KEY "sk-your-api-key-here"
```
6. **Install via pipx**
```bash
   pipx install .
```
7. **Restart your terminal**  
   You're ready to start using **GNote**!

---

💡 **Tip:** Run `note` anytime to open or append to your daily note, and `notesum` to get quick summaries powered by AI.
