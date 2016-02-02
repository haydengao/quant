import myapp as ma
import datetime

ma.db.create_all()

sttg1 = ma.Strategy(name='恶魔最摇摆', status='正常', start=datetime.date(2016,1,27))
sttg2 = ma.Strategy(name='音浪太强', status='正常', start=datetime.date(2016,1,28))

ma.db.session.add(sttg1)
ma.db.session.add(sttg2)
ma.db.session.commit()

sv1_0127 = ma.Survey(date=datetime.date(2016,1,27), daily=-1.3, profit=-1.3, sharp=1.1, marketValue=9233403, enable=2300, pullback=1.3, alpha=-1.3, beta=1.2, information=1.4, fluctuation=1.5, strategy_id=1)
sv1_0128 = ma.Survey(date=datetime.date(2016,1,28), daily=2.3, profit=2.01, sharp=2.1, marketValue=9800001, enable=2300, pullback=0, alpha=2.01, beta=2.2, information=2.4, fluctuation=2.5, strategy_id=1)
sv1_0129 = ma.Survey(date=datetime.date(2016,1,29), daily=3.3, profit=3.2, sharp=3.1, marketValue=9999403, enable=2300, pullback=0, alpha=3.4, beta=3.5, information=3.6, fluctuation=3.7, strategy_id=1)
sv2_0128 = ma.Survey(date=datetime.date(2016,1,28), daily=-1.4, profit=-1.4, sharp=1.2, marketValue=233403, enable=300, pullback=1.4, alpha=-1.4, beta=1.2, information=1.05, fluctuation=1.05, strategy_id=2)
sv2_0129 = ma.Survey(date=datetime.date(2016,1,29), daily=2.04, profit=2.14, sharp=2.2, marketValue=333403, enable=300, pullback=0, alpha=2.04, beta=2.2, information=2.05, fluctuation=2.05, strategy_id=2)

ma.db.session.add(sv1_0127)
ma.db.session.add(sv1_0128)
ma.db.session.add(sv1_0129)
ma.db.session.add(sv2_0128)
ma.db.session.add(sv2_0129)
ma.db.session.commit()

ps1_0127_1 = ma.Position(ticker='000632', name='三木集团', amount=1900, cost=6.82, price=6.96, value=13224, increase=1.97, weight=13.48,strategy_id=1, date_id=ma.Survey.query.filter_by(date=datetime.date(2016,1,27)).id)
ps1_0127_2 = ma.Position(ticker='002388', name='新亚制程', amount=1900, cost=7.11, price=7.28, value=13832, increase=2.39, weight=14.10,strategy_id=1, date_id=ma.Survey.query.filter_by(date=datetime.date(2016,1,27)).id)
ps1_0128_1 = ma.Position(ticker='600287', name='江苏舜天', amount=1800, cost=7.32, price=7.55, value=13590, increase=3.14, weight=13.85,strategy_id=1, date_id=ma.Survey.query.filter_by(date=datetime.date(2016,1,28)).id)
ps1_0128_2 = ma.Position(ticker='600731', name='湖南海利', amount=1800, cost=7.27, price=7.51, value=13518, increase=3.30, weight=13.78,strategy_id=1, date_id=ma.Survey.query.filter_by(date=datetime.date(2016,1,28)).id)
ps1_0129_1 = ma.Position(ticker='000890', name='法尔胜', amount=1600, cost=8.1, price=8.37, value=13392, increase=3.33, weight=13.65,strategy_id=1, date_id=ma.Survey.query.filter_by(date=datetime.date(2016,1,29)).id)
ps1_0129_2 = ma.Position(ticker='300084', name='海默科技', amount=1700, cost=7.8, price=8.17, value=13889, increase=4.74, weight=14.16,strategy_id=1, date_id=ma.Survey.query.filter_by(date=datetime.date(2016,1,29)).id)

ps2_0128_1 = ma.Position(ticker='002578', name='闽发铝业', amount=1700, cost=7.48, price=7.87, value=13379, increase=5.21, weight=13.64,strategy_id=2, date_id=ma.Survey.query.filter_by(date=datetime.date(2016,1,28)).id)
ps2_0128_2 = ma.Position(ticker='600731', name='湖南海利', amount=1800, cost=7.27, price=7.51, value=13518, increase=3.30, weight=13.78,strategy_id=2, date_id=ma.Survey.query.filter_by(date=datetime.date(2016,1,28)).id)
ps2_0129_1 = ma.Position(ticker='300237', name='美晨科技', amount=58700, cost=7.88, price=8.25, value=484275, increase=7.56, weight=48.88,strategy_id=2, date_id=ma.Survey.query.filter_by(date=datetime.date(2016,1,29)).id)
ps2_0129_2 = ma.Position(ticker='300084', name='海默科技', amount=1700, cost=7.8, price=8.17, value=13889, increase=4.74, weight=14.16,strategy_id=2, date_id=ma.Survey.query.filter_by(date=datetime.date(2016,1,29)).id)

ma.db.session.add(ps1_0127_1)
ma.db.session.add(ps1_0127_2)
ma.db.session.add(ps1_0128_1)
ma.db.session.add(ps1_0128_2)
ma.db.session.add(ps1_0129_1)
ma.db.session.add(ps1_0129_2)
ma.db.session.add(ps2_0128_1)
ma.db.session.add(ps2_0128_2)
ma.db.session.add(ps2_0129_1)
ma.db.session.add(ps2_0129_2)
ma.db.session.commit()

bm0127 = ma.Benchmark(date=datetime.date(2016,1,27), index=2735.558)
bm0128 = ma.Benchmark(date=datetime.date(2016,1,28), index=2655.661)
bm0129 = ma.Benchmark(date=datetime.date(2016,1,29), index=2737.6)

ma.db.session.add(bm0127)
ma.db.session.add(bm0128)
ma.db.session.add(bm0129)
ma.db.session.commit()