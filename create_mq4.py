# create_mq4.py

def create_mq4_file(file_path, bot_name, id, gmail, expiration_time):
    """Tạo một tệp .mq4 với cấu trúc cơ bản bao gồm thông số id, gmail, và thời gian hết hạn"""
    content = f"""
//+------------------------------------------------------------------+
//|                                                        {bot_name}.mq4 |
//|                        Copyright 2024, MyCompany                 |
//|                                       http://www.mycompany.net   |
//+------------------------------------------------------------------+
#property strict

// Thông số cấu hình
input string ID = "{id}";
input string Gmail = "{gmail}";
input string ExpirationTime = "{expiration_time}";

int OnInit()
  {{
   Print("Bot ID: {id}");
   Print("Gmail: {gmail}");
   Print("Expiration Time: {expiration_time}");
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
   Print("Deinitializing bot with ID: {id}");
   // TODO: Add your code here
  }}
//+------------------------------------------------------------------+
"""
    # Tạo tệp .mq4 và ghi nội dung vào tệp
    with open(file_path, "w", encoding="utf-8") as mq4_file:
        mq4_file.write(content)
    print(f"Đã tạo tệp {file_path} thành công!")
