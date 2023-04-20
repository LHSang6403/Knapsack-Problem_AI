docker build -t brute-img .

docker run -itd -v "$(pwd)/code:/usr/code" --name "brute" brute-img 
