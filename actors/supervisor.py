import os
print("Starting pipeline...")
os.system("python actors/prompt_response_loader/main.py")
os.system("python actors/quality_judge/main.py")
os.system("python actors/report_generator/main.py")
print("Pipeline completed.")
