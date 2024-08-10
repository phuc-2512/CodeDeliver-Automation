from signal_bot import check_signal
from auto_update_bot import auto_update_bot
from data_fetcher import fetch_latest_data

check_signal();
fetch_latest_data();
auto_update_bot()