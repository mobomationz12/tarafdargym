from python: latest
COPY bot.py .
RUN pip3 install requests rubika mutagen gtts pillow re PIL --upgrade
ENTRYPOINT [ "python3" ]
CMD ["bot.py"]