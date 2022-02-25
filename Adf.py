if __name__ == "__main__":
   try:
       __import__("ADF").ash_menu()
   except Exception as e:
       exit(str(e))