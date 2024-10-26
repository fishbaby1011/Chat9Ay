# ChatGay - A Fun Discord Bot for Nonsense Responses

ChatGay 是一個 Discord 機器人，用來在被提及時發送隨機的搞笑或無意義回覆。這個機器人使用了 `nonsense_phrases.txt` 文件中的隨機語錄，適合為伺服器增添一點趣味。
至於我為什麼會去寫這個呢，我也不知道，朋友提議我就寫出來了，~~順便練練我的python~~
## 功能
- 當用戶提及機器人時，ChatGay 會從 `nonsense_phrases.txt` 中選取隨機內容回覆。
- 支援基於 Discord API 的簡單命令，易於配置與運行。

## 文件說明
- `chatgay.py`：主程式碼，負責管理機器人的事件及回應機制。
- `nonsense_phrases.txt`：隨機回覆的內容來源，包含搞笑和無意義的短語。

## 安裝與設定
1. 確保 Python 版本為 3.8 或以上，並已安裝 Discord.py：
   ```bash
   pip install discord.py
   ```
2.將專案複製到你的工作目錄：
   ```bash
git clone https://github.com/yourusername/ChatGay.git
cd ChatGay
   ```
3.將機器人的 Token 放入 chatgay.py 中（請記得將預設 Token 替換為你自己的）。
4.啟動機器人：
   ```bash
python chatgay.py
   ```
