:mod:`koapy.cli`
================

.. py:module:: koapy.cli

.. autoapi-nested-parse::

   Console script for koapy.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   koapy.cli.fail_with_usage
   koapy.cli.cli
   koapy.cli.serve
   koapy.cli.login
   koapy.cli.config
   koapy.cli.autologin
   koapy.cli.update
   koapy.cli.trdata
   koapy.cli.realdata
   koapy.cli.version
   koapy.cli.get
   koapy.cli.stockcode
   koapy.cli.stockname
   koapy.cli.stockinfo
   koapy.cli.daily
   koapy.cli.minute
   koapy.cli.trinfo
   koapy.cli.realinfo
   koapy.cli.holidays
   koapy.cli.userinfo
   koapy.cli.deposit
   koapy.cli.evaluation
   koapy.cli.orders
   koapy.cli.modulepath
   koapy.cli.errmsg
   koapy.cli.watch
   koapy.cli.order
   koapy.cli.main



Attributes
~~~~~~~~~~

.. autoapisummary::

   koapy.cli.logger
   koapy.cli.context_settings
   koapy.cli.client_check_timeout
   koapy.cli.default_verbosity
   koapy.cli.default_verbosity_no_output
   koapy.cli.market_codes
   koapy.cli.minute_intervals
   koapy.cli.order_types
   koapy.cli.quote_types


.. data:: logger
   

   

.. data:: context_settings
   

   

.. data:: client_check_timeout
   :annotation: = 10

   

.. data:: default_verbosity
   :annotation: = 0

   

.. data:: default_verbosity_no_output
   :annotation: = 5

   

.. function:: fail_with_usage(message=None)


.. function:: cli()


.. function:: serve(port, verbose, no_verbose, args)


.. function:: login(port, verbose)


.. function:: config()


.. function:: autologin(port, verbose)


.. function:: update()


.. function:: trdata(verbose)


.. function:: realdata(verbose)


.. function:: version(verbose, no_verbose)


.. function:: get()


.. data:: market_codes
   :annotation: = ['0', '10', '3', '8', '50', '4', '5', '6', '9', '30', 'all']

   

.. function:: stockcode(names, markets, port)

   
   Possible market codes are:
     0 : 장내
     10 : 코스닥
     3 : ELW
     8 : ETF
     50 : KONEX
     4 : 뮤추얼펀드
     5 : 신주인수권
     6 : 리츠
     9 : 하이얼펀드
     30 : K-OTC

   
   Possible market code aliases are:
     all: All possible market codes.


.. function:: stockname(codes, port)


.. function:: stockinfo(code, output, format, port, verbose)


.. function:: daily(code, output, format, start_date, end_date, port, verbose)


.. data:: minute_intervals
   :annotation: = ['1', '3', '5', '10', '15', '30', '45', '60']

   

.. function:: minute(code, interval, output, format, start_date, end_date, port, verbose)


.. function:: trinfo(trcodes)


.. function:: realinfo(realtypes)


.. function:: holidays(output, offline, verbose)


.. function:: userinfo(port, verbose)


.. function:: deposit(account, port, verbose)


.. function:: evaluation(account, include_delisted, exclude_delisted, for_each, as_summary, port, verbose)


.. function:: orders(account, date, reverse, executed_only, not_executed_only, stock_only, bond_only, sell_only, buy_only, code, starting_order_no, port, verbose)


.. function:: modulepath(verbose)


.. function:: errmsg(err_code, verbose)


.. function:: watch(codes, input, fids, realtype, output, format, port, verbose)


.. data:: order_types
   :annotation: = ['1', '2', '3', '4', '5', '6']

   

.. data:: quote_types
   :annotation: = ['00', '03', '05', '06', '07', '10', '13', '16', '20', '23', '26', '61', '62', '81']

   

.. function:: order(request_name, screen_no, account_no, order_type, code, quantity, price, quote_type, original_order_no, format, port, verbose)

   
   [주문유형]
     1 : 신규매수
     2 : 신규매도
     3 : 매수취소
     4 : 매도취소
     5 : 매수정정
     6 : 매도정정

   
   [거래구분]
     모의투자에서는 지정가 주문과 시장가 주문만 가능합니다.
     00 : 지정가
     03 : 시장가
     05 : 조건부지정가
     06 : 최유리지정가
     07 : 최우선지정가
     10 : 지정가IOC
     13 : 시장가IOC
     16 : 최유리IOC
     20 : 지정가FOK
     23 : 시장가FOK
     26 : 최유리FOK
     61 : 장전시간외종가
     62 : 시간외단일가매매
     81 : 장후시간외종가


.. function:: main()


