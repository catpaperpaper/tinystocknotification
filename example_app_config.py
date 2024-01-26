FINN_KEY = 'finnhub_api_key'
SYMBOLS = [
        {'sym':'AAPL', 'max':187.99, 'min': 100},
        {'sym':'MSFT', 'max':400, 'min': 300}
        ]
# PROD sends emails
ENV = 'TEST'
EM = 'smtp_email_address_here'
EM_KEY = 'smtp_email_password_here'
# Subject is overwritten with max/min - example AAPL at 188.63, max of 187.99
EM_SUBJ = 'Hello, world.'
# This is the default body message 
EM_BODY = 'It''s not that I''m lazy, it''s that I''m highly efficient in my use of energy. Why walk when I can sit? Why sit when I can lie down? Why lie down when I can be unconscious?'
EM_RECP = 'recipient_email@domain.com'
SMTP = 'smtp.mail.domain.com'
SMTP_PORT = '465'
