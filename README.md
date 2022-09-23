# streamlabs-counter
Offline Counter for Streamlabs.

# Download
[Releases page](https://github.com/Lexer727/streamlabs-counter/releases/tag/v1.0.0)


# Build yourself
Build with: python -m PyInstaller --onefile --noconsole --icon=app.ico --add-data="app.ico;." counter.py

or: python -m PyInstaller .\counter.spec

# Setup Streamlabs
Integrate into Streamlabs:

1. Create Text (GDI+)

2. Enable Read from file

3. Set path to counter.txt (created by the program in the same folder as the program)

![image](https://user-images.githubusercontent.com/82832101/192057938-70968f6d-0f77-42bf-8495-6f4c5a0f6302.png)
