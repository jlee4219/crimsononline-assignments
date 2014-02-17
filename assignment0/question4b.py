def probability():
    # P(randint not being 0) = .80
    # P(player staying in for 5 rounds) = (.80)^5
    # P(player losing in 5 rounds) = (1 - (.80)^5)
    # P(all 3 losing) = (1 - (.80)^5) ^ 3
    print (1 - (.80) ** 5) ** 3