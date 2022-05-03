# https://inventwithpython.com/bigbookpython/project57.html

import random
import time

BAR = chr(9608)


def main():
    # simuler le téléchargement
    print("Downloading...")
    bytesDownloaded = 0  # prog init
    downloadSize = 2048  # total téléchargé
    while bytesDownloaded < downloadSize:
        bytesDownloaded += random.randint(0, 100)

        barStr = getProgressBar(bytesDownloaded, downloadSize)
        print(barStr, end='', flush=True)
        time.sleep(0.2)
        print('\b' * len(barStr), end= '', flush=True)


def getProgressBar(progress, total, barWidth=40):
    progressBar = ''
    progressBar += '['

    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    numberOfBars = int((progress/total) * barWidth)

    progressBar += BAR * numberOfBars
    progressBar += ' ' * (barWidth - numberOfBars)
    progressBar += ']'

    percentComplete = round(progress / total * 100), 1
    progressBar += ' ' + str(percentComplete) + '%'

    progressBar += ' ' + str(progress) + '/' + str(total)

    return progressBar


if __name__ == '__main__':
    main()
