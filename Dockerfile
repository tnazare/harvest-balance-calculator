FROM williamlauze/harvest-balance-calculator-infra:latest

COPY . /www

WORKDIR www

CMD python3 main.py