# Hello, I'm Shmalexa

- I cost you nothing (in money terms);
- I am customizable;
- I understand some of what you're saying;
- I require no internet connection, but human connection is very important to me;
- Say "Hey, Babe", if you want my attention;
- Say "Never mind", if you don't need anything right now;
- Say "Terminate", if you want me to leave you for a while;

# Here is my API, if you want to extend me:

I search for plugins in `~/.local/shmalexa`

- If you want to use custom directory, pass `SCRIPTS=<your directory>` before calling me;
- I will tell you what directory I'm using;
- Every plugin must contain function of the following signature:

`shmalexa(text, shm: Shmalexa) -> bool`

- `text` is my version of what you've said. Don't get upset when I get it wrong, you can always clarify yourself;
- `shm` - this is me;

`Shmalexa.capture(self) -> dict`

- I will return you some JSON; Access `return['text']` to get my version of your perspective (hmm... Sounds complicated)
