from gym.envs.registration import register
register(
    id='CREDITCARDFRAUD-v0',
    entry_point='env.credit_card_fraud_env:FraudEnv',
)