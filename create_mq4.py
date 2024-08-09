# create_mq4.py

def create_mq4_file(file_path, bot_name):
    """Tạo một tệp .mq4 với cấu trúc cơ bản bao gồm các thông số id, gmail, và thời gian hết hạn"""
    content = f"""
//+------------------------------------------------------------------+
//|                                                        {bot_name}.mq4 |
//|                        Copyright 2024, MyCompany                 |
//|                                       http://www.mycompany.net   |
//+------------------------------------------------------------------+
#property strict

// Thông số cấu hình
input string ID = "";
input string Gmail = "";
input string ExpirationTime = "";

int OnInit()
  {{
   Print("Bot ID: ", ID);
   Print("Gmail: ", Gmail);
   Print("Expiration Time: ", ExpirationTime);
   // TODO: Add your code here
   return(INIT_SUCCEEDED);
  }}

//+------------------------------------------------------------------+
int OnTick()
  {{
   // TODO: Add your code here
   return(0);
  }}

//+------------------------------------------------------------------+
void OnDeinit(const int reason)
  {{
   Print("Deinitializing bot with ID: ", ID);
   // TODO: Add your code here
  }}
//+------------------------------------------------------------------+
"""
    # Tạo tệp .mq4 và ghi nội dung vào tệp
    with open(file_path, "w", encoding="utf-8") as mq4_file:
        mq4_file.write(content)
    print(f"Đã tạo tệp {file_path} thành công!")
