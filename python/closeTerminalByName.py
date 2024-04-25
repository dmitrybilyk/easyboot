import psutil

def close_terminals_with_word(word):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.name() == 'xfce4-terminal':
            cmdline = ' '.join(proc.cmdline())
            if word.lower() in cmdline.lower():
                print(f"Closing terminal process: {proc.pid}")
                proc.terminate()

close_terminals_with_word('encourage')
