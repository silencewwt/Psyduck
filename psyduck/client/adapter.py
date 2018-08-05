"""
BitMEX API

## REST API for the BitMEX Trading Platform

[View Changelog](/app/apiChangelog)

----

#### Getting Started

Base URI: [https://www.bitmex.com/api/v1](/api/v1)

##### Fetching Data

All REST endpoints are documented below. You can try out any query right from this interface.

Most table queries accept `count`, `start`, and `reverse` params. Set `reverse=true` to get rows newest-first.

Additional documentation regarding filters, timestamps, and authentication
is available in [the main API documentation](/app/restAPI).

*All* table data is available via the [Websocket](/app/wsAPI). We highly recommend using the socket if you want
to have the quickest possible data without being subject to ratelimits.

##### Return Types

By default, all data is returned as JSON. Send `?_format=csv` to get CSV data or `?_format=xml` to get XML data.

##### Trade Data Queries

*This is only a small subset of what is available, to get you started.*

Fill in the parameters and click the `Try it out!` button to try any of these queries.

* [Pricing Data](#!/Quote/Quote_get)

* [Trade Data](#!/Trade/Trade_get)

* [OrderBook Data](#!/OrderBook/OrderBook_getL2)

* [Settlement Data](#!/Settlement/Settlement_get)

* [Exchange Statistics](#!/Stats/Stats_history)

Every function of the BitMEX.com platform is exposed here and documented. Many more functions are available.

##### Swagger Specification

[⇩ Download Swagger JSON](swagger.json)

----

## All API Endpoints

Click to expand a section.

"""

from psyduck.client.meta import RequestMeta


class BitmexAdapter(metaclass=RequestMeta):
    def __init__(self, client):
        self.client = client

    def get_announcement(self, columns=None):
        """
        Get site announcements.
        
        :param columns: Array of column names to fetch. If omitted, will return all columns.
        """
        return self.client.Announcement.Announcement_get(
            columns=columns).result()

    def get_announcement_urgent(self):
        """
        Get urgent (banner) announcements.
        
        """
        return self.client.Announcement.Announcement_getUrgent().result()

    def new_api_key(self,
                    name=None,
                    cidr=None,
                    permissions=None,
                    enabled=None,
                    token=None):
        """
        Create a new API Key.
        
        :param name: Key name. This name is for reference only.
        :param cidr: CIDR block to restrict this key to. To restrict to a single address, append "/32", e.g. 207.39.29.22/32. Leave blank or set to 0.0.0.0/0 to allow all IPs. Only one block may be set. <a href="http://software77.net/cidr-101.html">More on CIDR blocks</a>
        :param permissions: Key Permissions. All keys can read margin and position data. Additional permissions must be added. Available: ["order", "orderCancel", "withdraw"].
        :param enabled: Set to true to enable this key on creation. Otherwise, it must be explicitly enabled via /apiKey/enable.
        :param token: OTP Token (YubiKey, Google Authenticator)
        """
        return self.client.APIKey.APIKey_new(
            name=name,
            cidr=cidr,
            permissions=permissions,
            enabled=enabled,
            token=token).result()

    def get_api_key(self, reverse=None):
        """
        Get your API Keys.
        
        :param reverse: If true, will sort results newest first.
        """
        return self.client.APIKey.APIKey_get(reverse=reverse).result()

    def remove_api_key(self, api_key_id):
        """
        Remove an API Key.
        
        :param api_key_id: API Key ID (public component).
        """
        return self.client.APIKey.APIKey_remove(apiKeyID=api_key_id).result()

    def disable_api_key(self, api_key_id):
        """
        Disable an API Key.
        
        :param api_key_id: API Key ID (public component).
        """
        return self.client.APIKey.APIKey_disable(apiKeyID=api_key_id).result()

    def enable_api_key(self, api_key_id):
        """
        Enable an API Key.
        
        :param api_key_id: API Key ID (public component).
        """
        return self.client.APIKey.APIKey_enable(apiKeyID=api_key_id).result()

    def get_chat(self, count=None, start=None, reverse=None, channel_id=None):
        """
        Get chat messages.
        
        :param count: Number of results to fetch.
        :param start: Starting ID for results.
        :param reverse: If true, will sort results newest first.
        :param channel_id: Channel id. GET /chat/channels for ids. Leave blank for all.
        """
        return self.client.Chat.Chat_get(
            count=count, start=start, reverse=reverse,
            channelID=channel_id).result()

    def new_chat(self, message, channel_id=None):
        """
        Send a chat message.
        
        :param message: 
        :param channel_id: Channel to post to. Default 1 (English).
        """
        return self.client.Chat.Chat_new(
            message=message, channelID=channel_id).result()

    def get_chat_channels(self):
        """
        Get available channels.
        
        """
        return self.client.Chat.Chat_getChannels().result()

    def get_chat_connected(self):
        """
        Get connected users.
        
        """
        return self.client.Chat.Chat_getConnected().result()

    def get_execution(self,
                      symbol=None,
                      filter=None,
                      columns=None,
                      count=None,
                      start=None,
                      reverse=None,
                      start_time=None,
                      end_time=None):
        """
        Get all raw executions for your account.
        
        :param symbol: Instrument symbol. Send a bare series (e.g. XBU) to get data for the nearest expiring contract in that series.
        You can also send a timeframe, e.g. `XBU:monthly`. Timeframes are `daily`, `weekly`, `monthly`, `quarterly`, and `biquarterly`.
        :param filter: Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individual fields, and do more advanced querying on timestamps. See the [Timestamp Docs](https://www.bitmex.com/app/restAPI#Timestamp-Filters) for more details.
        :param columns: Array of column names to fetch. If omitted, will return all columns.
        Note that this method will always return item keys, even when not specified, so you may receive more columns that you expect.
        :param count: Number of results to fetch.
        :param start: Starting point for results.
        :param reverse: If true, will sort results newest first.
        :param start_time: Starting date filter for results.
        :param end_time: Ending date filter for results.
        """
        return self.client.Execution.Execution_get(
            symbol=symbol,
            filter=filter,
            columns=columns,
            count=count,
            start=start,
            reverse=reverse,
            startTime=start_time,
            endTime=end_time).result()

    def get_execution_trade_history(self,
                                    symbol=None,
                                    filter=None,
                                    columns=None,
                                    count=None,
                                    start=None,
                                    reverse=None,
                                    start_time=None,
                                    end_time=None):
        """
        Get all balance-affecting executions. This includes each trade, insurance charge, and settlement.
        
        :param symbol: Instrument symbol. Send a bare series (e.g. XBU) to get data for the nearest expiring contract in that series.
        You can also send a timeframe, e.g. `XBU:monthly`. Timeframes are `daily`, `weekly`, `monthly`, `quarterly`, and `biquarterly`.
        :param filter: Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individual fields, and do more advanced querying on timestamps. See the [Timestamp Docs](https://www.bitmex.com/app/restAPI#Timestamp-Filters) for more details.
        :param columns: Array of column names to fetch. If omitted, will return all columns.
        Note that this method will always return item keys, even when not specified, so you may receive more columns that you expect.
        :param count: Number of results to fetch.
        :param start: Starting point for results.
        :param reverse: If true, will sort results newest first.
        :param start_time: Starting date filter for results.
        :param end_time: Ending date filter for results.
        """
        return self.client.Execution.Execution_getTradeHistory(
            symbol=symbol,
            filter=filter,
            columns=columns,
            count=count,
            start=start,
            reverse=reverse,
            startTime=start_time,
            endTime=end_time).result()

    def get_funding(self,
                    symbol=None,
                    filter=None,
                    columns=None,
                    count=None,
                    start=None,
                    reverse=None,
                    start_time=None,
                    end_time=None):
        """
        Get funding history.
        
        :param symbol: Instrument symbol. Send a bare series (e.g. XBU) to get data for the nearest expiring contract in that series.
        You can also send a timeframe, e.g. `XBU:monthly`. Timeframes are `daily`, `weekly`, `monthly`, `quarterly`, and `biquarterly`.
        :param filter: Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individual fields, and do more advanced querying on timestamps. See the [Timestamp Docs](https://www.bitmex.com/app/restAPI#Timestamp-Filters) for more details.
        :param columns: Array of column names to fetch. If omitted, will return all columns.
        Note that this method will always return item keys, even when not specified, so you may receive more columns that you expect.
        :param count: Number of results to fetch.
        :param start: Starting point for results.
        :param reverse: If true, will sort results newest first.
        :param start_time: Starting date filter for results.
        :param end_time: Ending date filter for results.
        """
        return self.client.Funding.Funding_get(
            symbol=symbol,
            filter=filter,
            columns=columns,
            count=count,
            start=start,
            reverse=reverse,
            startTime=start_time,
            endTime=end_time).result()

    def get_instrument(self,
                       symbol=None,
                       filter=None,
                       columns=None,
                       count=None,
                       start=None,
                       reverse=None,
                       start_time=None,
                       end_time=None):
        """
        Get instruments.
        
        :param symbol: Instrument symbol. Send a bare series (e.g. XBU) to get data for the nearest expiring contract in that series.
        You can also send a timeframe, e.g. `XBU:monthly`. Timeframes are `daily`, `weekly`, `monthly`, `quarterly`, and `biquarterly`.
        :param filter: Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individual fields, and do more advanced querying on timestamps. See the [Timestamp Docs](https://www.bitmex.com/app/restAPI#Timestamp-Filters) for more details.
        :param columns: Array of column names to fetch. If omitted, will return all columns.
        Note that this method will always return item keys, even when not specified, so you may receive more columns that you expect.
        :param count: Number of results to fetch.
        :param start: Starting point for results.
        :param reverse: If true, will sort results newest first.
        :param start_time: Starting date filter for results.
        :param end_time: Ending date filter for results.
        """
        return self.client.Instrument.Instrument_get(
            symbol=symbol,
            filter=filter,
            columns=columns,
            count=count,
            start=start,
            reverse=reverse,
            startTime=start_time,
            endTime=end_time).result()

    def get_instrument_active(self):
        """
        Get all active instruments and instruments that have expired in <24hrs.
        
        """
        return self.client.Instrument.Instrument_getActive().result()

    def get_instrument_indices(self):
        """
        Get all price indices.
        
        """
        return self.client.Instrument.Instrument_getIndices().result()

    def get_instrument_active_and_indices(self):
        """
        Helper method. Gets all active instruments and all indices. This is a join of the result of /indices and /active.
        
        """
        return self.client.Instrument.Instrument_getActiveAndIndices().result()

    def get_instrument_active_intervals(self):
        """
        Return all active contract series and interval pairs.
        
        """
        return self.client.Instrument.Instrument_getActiveIntervals().result()

    def get_instrument_composite_index(self,
                                       symbol=None,
                                       filter=None,
                                       columns=None,
                                       count=None,
                                       start=None,
                                       reverse=None,
                                       start_time=None,
                                       end_time=None):
        """
        Show constituent parts of an index.
        
        :param symbol: The composite index symbol.
        :param filter: Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individual fields, and do more advanced querying on timestamps. See the [Timestamp Docs](https://www.bitmex.com/app/restAPI#Timestamp-Filters) for more details.
        :param columns: Array of column names to fetch. If omitted, will return all columns.
        Note that this method will always return item keys, even when not specified, so you may receive more columns that you expect.
        :param count: Number of results to fetch.
        :param start: Starting point for results.
        :param reverse: If true, will sort results newest first.
        :param start_time: Starting date filter for results.
        :param end_time: Ending date filter for results.
        """
        return self.client.Instrument.Instrument_getCompositeIndex(
            symbol=symbol,
            filter=filter,
            columns=columns,
            count=count,
            start=start,
            reverse=reverse,
            startTime=start_time,
            endTime=end_time).result()

    def get_insurance(self,
                      symbol=None,
                      filter=None,
                      columns=None,
                      count=None,
                      start=None,
                      reverse=None,
                      start_time=None,
                      end_time=None):
        """
        Get insurance fund history.
        
        :param symbol: Instrument symbol. Send a bare series (e.g. XBU) to get data for the nearest expiring contract in that series.
        You can also send a timeframe, e.g. `XBU:monthly`. Timeframes are `daily`, `weekly`, `monthly`, `quarterly`, and `biquarterly`.
        :param filter: Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individual fields, and do more advanced querying on timestamps. See the [Timestamp Docs](https://www.bitmex.com/app/restAPI#Timestamp-Filters) for more details.
        :param columns: Array of column names to fetch. If omitted, will return all columns.
        Note that this method will always return item keys, even when not specified, so you may receive more columns that you expect.
        :param count: Number of results to fetch.
        :param start: Starting point for results.
        :param reverse: If true, will sort results newest first.
        :param start_time: Starting date filter for results.
        :param end_time: Ending date filter for results.
        """
        return self.client.Insurance.Insurance_get(
            symbol=symbol,
            filter=filter,
            columns=columns,
            count=count,
            start=start,
            reverse=reverse,
            startTime=start_time,
            endTime=end_time).result()

    def get_leaderboard(self, method=None):
        """
        Get current leaderboard.
        
        :param method: Ranking type. Options: "notional", "ROE"
        """
        return self.client.Leaderboard.Leaderboard_get(method=method).result()

    def get_leaderboard_name(self):
        """
        Get your alias on the leaderboard.
        
        """
        return self.client.Leaderboard.Leaderboard_getName().result()

    def get_liquidation(self,
                        symbol=None,
                        filter=None,
                        columns=None,
                        count=None,
                        start=None,
                        reverse=None,
                        start_time=None,
                        end_time=None):
        """
        Get liquidation orders.
        
        :param symbol: Instrument symbol. Send a bare series (e.g. XBU) to get data for the nearest expiring contract in that series.
        You can also send a timeframe, e.g. `XBU:monthly`. Timeframes are `daily`, `weekly`, `monthly`, `quarterly`, and `biquarterly`.
        :param filter: Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individual fields, and do more advanced querying on timestamps. See the [Timestamp Docs](https://www.bitmex.com/app/restAPI#Timestamp-Filters) for more details.
        :param columns: Array of column names to fetch. If omitted, will return all columns.
        Note that this method will always return item keys, even when not specified, so you may receive more columns that you expect.
        :param count: Number of results to fetch.
        :param start: Starting point for results.
        :param reverse: If true, will sort results newest first.
        :param start_time: Starting date filter for results.
        :param end_time: Ending date filter for results.
        """
        return self.client.Liquidation.Liquidation_get(
            symbol=symbol,
            filter=filter,
            columns=columns,
            count=count,
            start=start,
            reverse=reverse,
            startTime=start_time,
            endTime=end_time).result()

    def get_notification(self):
        """
        Get your current notifications.
        
        """
        return self.client.Notification.Notification_get().result()

    def get_orders(self,
                   symbol=None,
                   filter=None,
                   columns=None,
                   count=None,
                   start=None,
                   reverse=None,
                   start_time=None,
                   end_time=None):
        """
        Get your orders.
        
        :param symbol: Instrument symbol. Send a bare series (e.g. XBU) to get data for the nearest expiring contract in that series.
        You can also send a timeframe, e.g. `XBU:monthly`. Timeframes are `daily`, `weekly`, `monthly`, `quarterly`, and `biquarterly`.
        :param filter: Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individual fields, and do more advanced querying on timestamps. See the [Timestamp Docs](https://www.bitmex.com/app/restAPI#Timestamp-Filters) for more details.
        :param columns: Array of column names to fetch. If omitted, will return all columns.
        Note that this method will always return item keys, even when not specified, so you may receive more columns that you expect.
        :param count: Number of results to fetch.
        :param start: Starting point for results.
        :param reverse: If true, will sort results newest first.
        :param start_time: Starting date filter for results.
        :param end_time: Ending date filter for results.
        """
        return self.client.Order.Order_getOrders(
            symbol=symbol,
            filter=filter,
            columns=columns,
            count=count,
            start=start,
            reverse=reverse,
            startTime=start_time,
            endTime=end_time).result()

    def new_order(self,
                  symbol,
                  side=None,
                  simple_order_qty=None,
                  order_qty=None,
                  price=None,
                  display_qty=None,
                  stop_px=None,
                  cl_ord_id=None,
                  cl_ord_link_id=None,
                  peg_offset_value=None,
                  peg_price_type=None,
                  ord_type=None,
                  time_in_force=None,
                  exec_inst=None,
                  contingency_type=None,
                  text=None):
        """
        Create a new order.
        
        :param symbol: Instrument symbol. e.g. 'XBTUSD'.
        :param side: Order side. Valid options: Buy, Sell. Defaults to 'Buy' unless `orderQty` or `simpleOrderQty` is negative.
        :param simple_order_qty: Order quantity in units of the underlying instrument (i.e. Bitcoin).
        :param order_qty: Order quantity in units of the instrument (i.e. contracts).
        :param price: Optional limit price for 'Limit', 'StopLimit', and 'LimitIfTouched' orders.
        :param display_qty: Optional quantity to display in the book. Use 0 for a fully hidden order.
        :param stop_px: Optional trigger price for 'Stop', 'StopLimit', 'MarketIfTouched', and 'LimitIfTouched' orders. Use a price below the current price for stop-sell orders and buy-if-touched orders. Use `execInst` of 'MarkPrice' or 'LastPrice' to define the current price used for triggering.
        :param cl_ord_id: Optional Client Order ID. This clOrdID will come back on the order and any related executions.
        :param cl_ord_link_id: Optional Client Order Link ID for contingent orders.
        :param peg_offset_value: Optional trailing offset from the current price for 'Stop', 'StopLimit', 'MarketIfTouched', and 'LimitIfTouched' orders; use a negative offset for stop-sell orders and buy-if-touched orders. Optional offset from the peg price for 'Pegged' orders.
        :param peg_price_type: Optional peg price type. Valid options: LastPeg, MidPricePeg, MarketPeg, PrimaryPeg, TrailingStopPeg.
        :param ord_type: Order type. Valid options: Market, Limit, Stop, StopLimit, MarketIfTouched, LimitIfTouched, MarketWithLeftOverAsLimit, Pegged. Defaults to 'Limit' when `price` is specified. Defaults to 'Stop' when `stopPx` is specified. Defaults to 'StopLimit' when `price` and `stopPx` are specified.
        :param time_in_force: Time in force. Valid options: Day, GoodTillCancel, ImmediateOrCancel, FillOrKill. Defaults to 'GoodTillCancel' for 'Limit', 'StopLimit', 'LimitIfTouched', and 'MarketWithLeftOverAsLimit' orders.
        :param exec_inst: Optional execution instructions. Valid options: ParticipateDoNotInitiate, AllOrNone, MarkPrice, IndexPrice, LastPrice, Close, ReduceOnly, Fixed. 'AllOrNone' instruction requires `displayQty` to be 0. 'MarkPrice', 'IndexPrice' or 'LastPrice' instruction valid for 'Stop', 'StopLimit', 'MarketIfTouched', and 'LimitIfTouched' orders.
        :param contingency_type: Optional contingency type for use with `clOrdLinkID`. Valid options: OneCancelsTheOther, OneTriggersTheOther, OneUpdatesTheOtherAbsolute, OneUpdatesTheOtherProportional.
        :param text: Optional order annotation. e.g. 'Take profit'.
        """
        return self.client.Order.Order_new(
            symbol=symbol,
            side=side,
            simpleOrderQty=simple_order_qty,
            orderQty=order_qty,
            price=price,
            displayQty=display_qty,
            stopPx=stop_px,
            clOrdID=cl_ord_id,
            clOrdLinkID=cl_ord_link_id,
            pegOffsetValue=peg_offset_value,
            pegPriceType=peg_price_type,
            ordType=ord_type,
            timeInForce=time_in_force,
            execInst=exec_inst,
            contingencyType=contingency_type,
            text=text).result()

    def amend_order(self,
                    order_id=None,
                    orig_cl_ord_id=None,
                    cl_ord_id=None,
                    simple_order_qty=None,
                    order_qty=None,
                    simple_leaves_qty=None,
                    leaves_qty=None,
                    price=None,
                    stop_px=None,
                    peg_offset_value=None,
                    text=None):
        """
        Amend the quantity or price of an open order.
        
        :param order_id: Order ID
        :param orig_cl_ord_id: Client Order ID. See POST /order.
        :param cl_ord_id: Optional new Client Order ID, requires `origClOrdID`.
        :param simple_order_qty: Optional order quantity in units of the underlying instrument (i.e. Bitcoin).
        :param order_qty: Optional order quantity in units of the instrument (i.e. contracts).
        :param simple_leaves_qty: Optional leaves quantity in units of the underlying instrument (i.e. Bitcoin). Useful for amending partially filled orders.
        :param leaves_qty: Optional leaves quantity in units of the instrument (i.e. contracts). Useful for amending partially filled orders.
        :param price: Optional limit price for 'Limit', 'StopLimit', and 'LimitIfTouched' orders.
        :param stop_px: Optional trigger price for 'Stop', 'StopLimit', 'MarketIfTouched', and 'LimitIfTouched' orders. Use a price below the current price for stop-sell orders and buy-if-touched orders.
        :param peg_offset_value: Optional trailing offset from the current price for 'Stop', 'StopLimit', 'MarketIfTouched', and 'LimitIfTouched' orders; use a negative offset for stop-sell orders and buy-if-touched orders. Optional offset from the peg price for 'Pegged' orders.
        :param text: Optional amend annotation. e.g. 'Adjust skew'.
        """
        return self.client.Order.Order_amend(
            orderID=order_id,
            origClOrdID=orig_cl_ord_id,
            clOrdID=cl_ord_id,
            simpleOrderQty=simple_order_qty,
            orderQty=order_qty,
            simpleLeavesQty=simple_leaves_qty,
            leavesQty=leaves_qty,
            price=price,
            stopPx=stop_px,
            pegOffsetValue=peg_offset_value,
            text=text).result()

    def cancel_order(self, order_id=None, cl_ord_id=None, text=None):
        """
        Cancel order(s). Send multiple order IDs to cancel in bulk.
        
        :param order_id: Order ID(s).
        :param cl_ord_id: Client Order ID(s). See POST /order.
        :param text: Optional cancellation annotation. e.g. 'Spread Exceeded'.
        """
        return self.client.Order.Order_cancel(
            orderID=order_id, clOrdID=cl_ord_id, text=text).result()

    def new_order_bulk(self, orders=None):
        """
        Create multiple new orders for the same symbol.
        
        :param orders: An array of orders.
        """
        return self.client.Order.Order_newBulk(orders=orders).result()

    def amend_order_bulk(self, orders=None):
        """
        Amend multiple orders for the same symbol.
        
        :param orders: An array of orders.
        """
        return self.client.Order.Order_amendBulk(orders=orders).result()

    def close_order_position(self, symbol, price=None):
        """
        Close a position. [Deprecated, use POST /order with execInst: 'Close']
        
        :param symbol: Symbol of position to close.
        :param price: Optional limit price.
        """
        return self.client.Order.Order_closePosition(
            symbol=symbol, price=price).result()

    def cancel_order_all(self, symbol=None, filter=None, text=None):
        """
        Cancels all of your orders.
        
        :param symbol: Optional symbol. If provided, only cancels orders for that symbol.
        :param filter: Optional filter for cancellation. Use to only cancel some orders, e.g. `{"side": "Buy"}`.
        :param text: Optional cancellation annotation. e.g. 'Spread Exceeded'
        """
        return self.client.Order.Order_cancelAll(
            symbol=symbol, filter=filter, text=text).result()

    def cancel_order_all_after(self, timeout):
        """
        Automatically cancel all your orders after a specified timeout.
        
        :param timeout: Timeout in ms. Set to 0 to cancel this timer. 
        """
        return self.client.Order.Order_cancelAllAfter(timeout=timeout).result()

    def get_order_book_l2(self, symbol, depth=None):
        """
        Get current orderbook in vertical format.
        
        :param symbol: Instrument symbol. Send a series (e.g. XBT) to get data for the nearest contract in that series.
        :param depth: Orderbook depth per side. Send 0 for full depth.
        """
        return self.client.OrderBook.OrderBook_getL2(
            symbol=symbol, depth=depth).result()

    def get_position(self, filter=None, columns=None, count=None):
        """
        Get your positions.
        
        :param filter: Table filter. For example, send {"symbol": "XBTUSD"}.
        :param columns: Which columns to fetch. For example, send ["columnName"].
        :param count: Number of rows to fetch.
        """
        return self.client.Position.Position_get(
            filter=filter, columns=columns, count=count).result()

    def isolate_position_margin(self, symbol, enabled=None):
        """
        Enable isolated margin or cross margin per-position.
        
        :param symbol: Position symbol to isolate.
        :param enabled: True for isolated margin, false for cross margin.
        """
        return self.client.Position.Position_isolateMargin(
            symbol=symbol, enabled=enabled).result()

    def update_position_risk_limit(self, symbol, risk_limit):
        """
        Update your risk limit.
        
        :param symbol: Symbol of position to update risk limit on.
        :param risk_limit: New Risk Limit, in Satoshis.
        """
        return self.client.Position.Position_updateRiskLimit(
            symbol=symbol, riskLimit=risk_limit).result()

    def transfer_position_isolated_margin(self, symbol, amount):
        """
        Transfer equity in or out of a position.
        
        :param symbol: Symbol of position to isolate.
        :param amount: Amount to transfer, in Satoshis. May be negative.
        """
        return self.client.Position.Position_transferIsolatedMargin(
            symbol=symbol, amount=amount).result()

    def update_position_leverage(self, symbol, leverage):
        """
        Choose leverage for a position.
        
        :param symbol: Symbol of position to adjust.
        :param leverage: Leverage value. Send a number between 0.01 and 100 to enable isolated margin with a fixed leverage. Send 0 to enable cross margin.
        """
        return self.client.Position.Position_updateLeverage(
            symbol=symbol, leverage=leverage).result()

    def get_quote(self,
                  symbol=None,
                  filter=None,
                  columns=None,
                  count=None,
                  start=None,
                  reverse=None,
                  start_time=None,
                  end_time=None):
        """
        Get Quotes.
        
        :param symbol: Instrument symbol. Send a bare series (e.g. XBU) to get data for the nearest expiring contract in that series.
        You can also send a timeframe, e.g. `XBU:monthly`. Timeframes are `daily`, `weekly`, `monthly`, `quarterly`, and `biquarterly`.
        :param filter: Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individual fields, and do more advanced querying on timestamps. See the [Timestamp Docs](https://www.bitmex.com/app/restAPI#Timestamp-Filters) for more details.
        :param columns: Array of column names to fetch. If omitted, will return all columns.
        Note that this method will always return item keys, even when not specified, so you may receive more columns that you expect.
        :param count: Number of results to fetch.
        :param start: Starting point for results.
        :param reverse: If true, will sort results newest first.
        :param start_time: Starting date filter for results.
        :param end_time: Ending date filter for results.
        """
        return self.client.Quote.Quote_get(
            symbol=symbol,
            filter=filter,
            columns=columns,
            count=count,
            start=start,
            reverse=reverse,
            startTime=start_time,
            endTime=end_time).result()

    def get_quote_bucketed(self,
                           bin_size=None,
                           partial=None,
                           symbol=None,
                           filter=None,
                           columns=None,
                           count=None,
                           start=None,
                           reverse=None,
                           start_time=None,
                           end_time=None):
        """
        Get previous quotes in time buckets.
        
        :param bin_size: Time interval to bucket by. Available options: [1m,5m,1h,1d].
        :param partial: If true, will send in-progress (incomplete) bins for the current time period.
        :param symbol: Instrument symbol. Send a bare series (e.g. XBU) to get data for the nearest expiring contract in that series.
        You can also send a timeframe, e.g. `XBU:monthly`. Timeframes are `daily`, `weekly`, `monthly`, `quarterly`, and `biquarterly`.
        :param filter: Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individual fields, and do more advanced querying on timestamps. See the [Timestamp Docs](https://www.bitmex.com/app/restAPI#Timestamp-Filters) for more details.
        :param columns: Array of column names to fetch. If omitted, will return all columns.
        Note that this method will always return item keys, even when not specified, so you may receive more columns that you expect.
        :param count: Number of results to fetch.
        :param start: Starting point for results.
        :param reverse: If true, will sort results newest first.
        :param start_time: Starting date filter for results.
        :param end_time: Ending date filter for results.
        """
        return self.client.Quote.Quote_getBucketed(
            binSize=bin_size,
            partial=partial,
            symbol=symbol,
            filter=filter,
            columns=columns,
            count=count,
            start=start,
            reverse=reverse,
            startTime=start_time,
            endTime=end_time).result()

    def get_schema(self, model=None):
        """
        Get model schemata for data objects returned by this API.
        
        :param model: Optional model filter. If omitted, will return all models.
        """
        return self.client.Schema.Schema_get(model=model).result()

    def websocket_schema_help(self):
        """
        Returns help text & subject list for websocket usage.
        
        """
        return self.client.Schema.Schema_websocketHelp().result()

    def get_settlement(self,
                       symbol=None,
                       filter=None,
                       columns=None,
                       count=None,
                       start=None,
                       reverse=None,
                       start_time=None,
                       end_time=None):
        """
        Get settlement history.
        
        :param symbol: Instrument symbol. Send a bare series (e.g. XBU) to get data for the nearest expiring contract in that series.
        You can also send a timeframe, e.g. `XBU:monthly`. Timeframes are `daily`, `weekly`, `monthly`, `quarterly`, and `biquarterly`.
        :param filter: Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individual fields, and do more advanced querying on timestamps. See the [Timestamp Docs](https://www.bitmex.com/app/restAPI#Timestamp-Filters) for more details.
        :param columns: Array of column names to fetch. If omitted, will return all columns.
        Note that this method will always return item keys, even when not specified, so you may receive more columns that you expect.
        :param count: Number of results to fetch.
        :param start: Starting point for results.
        :param reverse: If true, will sort results newest first.
        :param start_time: Starting date filter for results.
        :param end_time: Ending date filter for results.
        """
        return self.client.Settlement.Settlement_get(
            symbol=symbol,
            filter=filter,
            columns=columns,
            count=count,
            start=start,
            reverse=reverse,
            startTime=start_time,
            endTime=end_time).result()

    def get_stats(self):
        """
        Get exchange-wide and per-series turnover and volume statistics.
        
        """
        return self.client.Stats.Stats_get().result()

    def history_stats(self):
        """
        Get historical exchange-wide and per-series turnover and volume statistics.
        
        """
        return self.client.Stats.Stats_history().result()

    def history_stats_usd(self):
        """
        Get a summary of exchange statistics in USD.
        
        """
        return self.client.Stats.Stats_historyUSD().result()

    def get_trade(self,
                  symbol=None,
                  filter=None,
                  columns=None,
                  count=None,
                  start=None,
                  reverse=None,
                  start_time=None,
                  end_time=None):
        """
        Get Trades.
        
        :param symbol: Instrument symbol. Send a bare series (e.g. XBU) to get data for the nearest expiring contract in that series.
        You can also send a timeframe, e.g. `XBU:monthly`. Timeframes are `daily`, `weekly`, `monthly`, `quarterly`, and `biquarterly`.
        :param filter: Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individual fields, and do more advanced querying on timestamps. See the [Timestamp Docs](https://www.bitmex.com/app/restAPI#Timestamp-Filters) for more details.
        :param columns: Array of column names to fetch. If omitted, will return all columns.
        Note that this method will always return item keys, even when not specified, so you may receive more columns that you expect.
        :param count: Number of results to fetch.
        :param start: Starting point for results.
        :param reverse: If true, will sort results newest first.
        :param start_time: Starting date filter for results.
        :param end_time: Ending date filter for results.
        """
        return self.client.Trade.Trade_get(
            symbol=symbol,
            filter=filter,
            columns=columns,
            count=count,
            start=start,
            reverse=reverse,
            startTime=start_time,
            endTime=end_time).result()

    def get_trade_bucketed(self,
                           bin_size=None,
                           partial=None,
                           symbol=None,
                           filter=None,
                           columns=None,
                           count=None,
                           start=None,
                           reverse=None,
                           start_time=None,
                           end_time=None):
        """
        Get previous trades in time buckets.
        
        :param bin_size: Time interval to bucket by. Available options: [1m,5m,1h,1d].
        :param partial: If true, will send in-progress (incomplete) bins for the current time period.
        :param symbol: Instrument symbol. Send a bare series (e.g. XBU) to get data for the nearest expiring contract in that series.
        You can also send a timeframe, e.g. `XBU:monthly`. Timeframes are `daily`, `weekly`, `monthly`, `quarterly`, and `biquarterly`.
        :param filter: Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individual fields, and do more advanced querying on timestamps. See the [Timestamp Docs](https://www.bitmex.com/app/restAPI#Timestamp-Filters) for more details.
        :param columns: Array of column names to fetch. If omitted, will return all columns.
        Note that this method will always return item keys, even when not specified, so you may receive more columns that you expect.
        :param count: Number of results to fetch.
        :param start: Starting point for results.
        :param reverse: If true, will sort results newest first.
        :param start_time: Starting date filter for results.
        :param end_time: Ending date filter for results.
        """
        return self.client.Trade.Trade_getBucketed(
            binSize=bin_size,
            partial=partial,
            symbol=symbol,
            filter=filter,
            columns=columns,
            count=count,
            start=start,
            reverse=reverse,
            startTime=start_time,
            endTime=end_time).result()

    def get_user_deposit_address(self, currency=None):
        """
        Get a deposit address.
        
        :param currency: 
        """
        return self.client.User.User_getDepositAddress(
            currency=currency).result()

    def get_user_wallet(self, currency=None):
        """
        Get your current wallet information.
        
        :param currency: 
        """
        return self.client.User.User_getWallet(currency=currency).result()

    def get_user_wallet_history(self, currency=None):
        """
        Get a history of all of your wallet transactions (deposits, withdrawals, PNL).
        
        :param currency: 
        """
        return self.client.User.User_getWalletHistory(
            currency=currency).result()

    def get_user_wallet_summary(self, currency=None):
        """
        Get a summary of all of your wallet transactions (deposits, withdrawals, PNL).
        
        :param currency: 
        """
        return self.client.User.User_getWalletSummary(
            currency=currency).result()

    def get_user_execution_history(self, symbol, timestamp):
        """
        Get the execution history by day.
        
        :param symbol: 
        :param timestamp: 
        """
        return self.client.User.User_getExecutionHistory(
            symbol=symbol, timestamp=timestamp).result()

    def min_user_withdrawal_fee(self, currency=None):
        """
        Get the minimum withdrawal fee for a currency.
        
        :param currency: 
        """
        return self.client.User.User_minWithdrawalFee(
            currency=currency).result()

    def request_user_withdrawal(self,
                                currency,
                                amount,
                                address,
                                otp_token=None,
                                fee=None):
        """
        Request a withdrawal to an external wallet.
        
        :param otp_token: 2FA token. Required if 2FA is enabled on your account.
        :param currency: Currency you're withdrawing. Options: `XBt`
        :param amount: Amount of withdrawal currency.
        :param address: Destination Address.
        :param fee: Network fee for Bitcoin withdrawals. If not specified, a default value will be calculated based on Bitcoin network conditions. You will have a chance to confirm this via email.
        """
        return self.client.User.User_requestWithdrawal(
            otpToken=otp_token,
            currency=currency,
            amount=amount,
            address=address,
            fee=fee).result()

    def cancel_user_withdrawal(self, token):
        """
        Cancel a withdrawal.
        
        :param token: 
        """
        return self.client.User.User_cancelWithdrawal(token=token).result()

    def confirm_user_withdrawal(self, token):
        """
        Confirm a withdrawal.
        
        :param token: 
        """
        return self.client.User.User_confirmWithdrawal(token=token).result()

    def request_user_enable_tfa(self, type=None):
        """
        Get secret key for setting up two-factor auth.
        
        :param type: Two-factor auth type. Supported types: 'GA' (Google Authenticator)
        """
        return self.client.User.User_requestEnableTFA(type=type).result()

    def confirm_user_enable_tfa(self, token, type=None):
        """
        Confirm two-factor auth for this account. If using a Yubikey, simply send a token to this endpoint.
        
        :param type: Two-factor auth type. Supported types: 'GA' (Google Authenticator), 'Yubikey'
        :param token: Token from your selected TFA type.
        """
        return self.client.User.User_confirmEnableTFA(
            type=type, token=token).result()

    def disable_user_tfa(self, token, type=None):
        """
        Disable two-factor auth for this account.
        
        :param type: Two-factor auth type. Supported types: 'GA' (Google Authenticator)
        :param token: Token from your selected TFA type.
        """
        return self.client.User.User_disableTFA(
            type=type, token=token).result()

    def confirm_user(self, token):
        """
        Confirm your email address with a token.
        
        :param token: 
        """
        return self.client.User.User_confirm(token=token).result()

    def get_user_affiliate_status(self):
        """
        Get your current affiliate/referral status.
        
        """
        return self.client.User.User_getAffiliateStatus().result()

    def check_user_referral_code(self, referral_code=None):
        """
        Check if a referral code is valid.
        
        :param referral_code: 
        """
        return self.client.User.User_checkReferralCode(
            referralCode=referral_code).result()

    def logout_user(self):
        """
        Log out of BitMEX.
        
        """
        return self.client.User.User_logout().result()

    def logout_user_all(self):
        """
        Log all systems out of BitMEX. This will revoke all of your account's access tokens, logging you out on all devices.
        
        """
        return self.client.User.User_logoutAll().result()

    def save_user_preferences(self, prefs, overwrite=None):
        """
        Save user preferences.
        
        :param prefs: 
        :param overwrite: If true, will overwrite all existing preferences.
        """
        return self.client.User.User_savePreferences(
            prefs=prefs, overwrite=overwrite).result()

    def get_user(self):
        """
        Get your user model.
        
        """
        return self.client.User.User_get().result()

    def update_user(self,
                    old_password=None,
                    new_password=None,
                    new_password_confirm=None,
                    username=None,
                    country=None,
                    pgp_pub_key=None):
        """
        Update your password, name, and other attributes.
        
        :param old_password: 
        :param new_password: 
        :param new_password_confirm: 
        :param username: Username can only be set once. To reset, email support.
        :param country: Country of residence.
        :param pgp_pub_key: PGP Public Key. If specified, automated emails will be sentwith this key.
        """
        return self.client.User.User_update(
            oldPassword=old_password,
            newPassword=new_password,
            newPasswordConfirm=new_password_confirm,
            username=username,
            country=country,
            pgpPubKey=pgp_pub_key).result()

    def get_user_commission(self):
        """
        Get your account's commission status.
        
        """
        return self.client.User.User_getCommission().result()

    def get_user_margin(self, currency=None):
        """
        Get your account's margin status. Send a currency of "all" to receive an array of all supported currencies.
        
        :param currency: 
        """
        return self.client.User.User_getMargin(currency=currency).result()
