docker build -t brute-img .

docker run -itd -v "./code:/usr/code" --name "brute" brute-img 
