:loop

taskkill /IM VPN.exe
taskkill /IM chrome.exe

echo "STARTING..."
cmd.exe /c " start C:\Users\Sophia\Downloads\YoutubeBot-main\Chrome\vpn.exe"

timeout 10

echo "[!] Acessando o video..."
cmd.exe /c "python C:\Users\Sophia\Downloads\YoutubeBot-main\Chrome\yt.py"

timeout 1

echo "[+] Visualização Completa."
taskkill /IM chrome.exe /F

timeout 1

echo " Finalizando a VPN"
taskkill /IM vpn.exe /F

goto loop

