from graph import app

def main():
    print("=================================================")
    print("🚀 MARKET PULSE: Enterprise Competitive Agent")
    print("Powered by Gemini 1.5 Pro & LangGraph")
    print("=================================================")
    
    user_input = input("\nEnter a research topic (e.g., 'Tesla vs Rivian'): ")
    
    if not user_input:
        print("Please enter a valid topic.")
        return

    inputs = {"task": user_input}
    
    # Execute the graph
    result = app.invoke(inputs)
    
    print("\n\n" + "="*30)
    print("📊 FINAL EXECUTIVE REPORT")
    print("="*30 + "\n")
    print(result['final_report'])
    
    # Optional: Save to file
    with open("report.md", "w") as f:
        f.write(result['final_report'])
    print("\n✅ Report saved to 'report.md'")

if __name__ == "__main__":
    main()
