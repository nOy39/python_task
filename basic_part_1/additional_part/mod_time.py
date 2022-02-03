import time

"""Значение времени, возвращаемое gmtime(),localtime(), и strptime()
и принимаемое asctime(), mktime() и strftime(), 
представляет собой последовательность из 9 целых чисел. 
Возвращаемые значения gmtime(), localtime(), 
а strptime()также предлагают имена атрибутов для отдельных полей."""

"""DOCS"""


def _struct_time_doc():
    """
        class time.struct_time

        Index   Attribute   Values
        0       tm_year     (for example, 1993)
        1       tm_mon      range [1, 12]
        2       tm_mday     range [1, 31]
        3       tm_hour     range [0, 23]
        4       tm_min      range [0, 59]
        5       tm_sec      range [0, 61]; see (2) in strftime() description
        6       tm_wday     range [0, 6], Monday is 0
        8       tm_isdst    0, 1 or -1; see below
        N/A     tm_zone     abbreviation of timezone name
        N/A     tm_gmtoff   offset east of UTC in seconds
    """
    pass


def _strptime_doc(_str):
    """
    strptime(string, format) -> struct_time

        Parse a string to a time tuple according to a format specification.
        See the library reference manual for formatting codes (same as
        strftime()).

        Commonly used format codes:

        %Y  Year with century as a decimal number.
        %m  Month as a decimal number [01,12].
        %d  Day of the month as a decimal number [01,31].
        %H  Hour (24-hour clock) as a decimal number [00,23].
        %M  Minute as a decimal number [00,59].
        %S  Second as a decimal number [00,61].
        %z  Time zone offset from UTC.
        %a  Locale's abbreviated weekday name.
        %A  Locale's full weekday name.
        %b  Locale's abbreviated month name.
        %B  Locale's full month name.
        %c  Locale's appropriate date and time representation.
        %I  Hour (12-hour clock) as a decimal number [01,12].
        %p  Locale's equivalent of either AM or PM.

        Other codes may be available on your platform.  See documentation for
        the C library strftime function.

    :param _str: Date string format..
    :return: struct_time
    """
    pass


def _strftime_doc(_struct_time):
    """
    Convert a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string as specified by the format argument.
    If t is not provided, the current time as returned by localtime() is used. format must be a string.
    ValueError is raised if any field in t is outside of the allowed range.

    0 is a legal argument for any position in the time tuple;
    if it is normally illegal the value is forced to a correct one.

    The following directives can be embedded in the format string.
    They are shown without the optional field width and precision specification,
    and are replaced by the indicated characters in the strftime() result:


    Directive       Meaning                                                        Notes
    %a              Locale’s abbreviated weekday name.
    %A              Locale’s full weekday name.
    %b              Locale’s abbreviated month name.
    %B              Locale’s full month name.
    %c              Locale’s appropriate date and time representation.
    %d              Day of the month as a decimal number [01,31].
    %H              Hour (24-hour clock) as a decimal number [00,23].
    %I              Hour (12-hour clock) as a decimal number [01,12].
    %j              Day of the year as a decimal number [001,366].
    %m              Month as a decimal number [01,12].
    %M              Minute as a decimal number [00,59].
    %p              Locale’s equivalent of either AM or PM.                         (1)
    %S              Second as a decimal number [00,61].                             (2)
    %U              Week number of the year (Sunday as the first day of the week)
                    as a decimal number [00,53]. All days in a new year preceding
                    the first Sunday are considered to be in week 0.
    %w              Weekday as a decimal number [0(Sunday),6].                      (3)
    %W              Week number of the year (Monday as the first day of the week)
                    as a decimal number [00,53]. All days in a new year preceding
                    the first Monday are considered to be in week 0.                (3)
    %x              Locale’s appropriate date representation.
    %X              Locale’s appropriate time representation.
    %y              Year without century as a decimal number [00,99].
    %Y              Year with century as a decimal number.
    %z              Time zone offset indicating a positive or negative time
                    difference from UTC/GMT of the form +HHMM or -HHMM,
                    where H represents decimal hour digits and M represents decimal
                    minute digits [-23:59, +23:59].
    %%              A literal '%' character.

    :param _struct_time:
    :return:
    """


def _gmtime_doc(_float):
    """

        gmtime([seconds]) -> (tm_year, tm_mon, tm_mday, tm_hour, tm_min,
                           tm_sec, tm_wday, tm_yday, tm_isdst)

        Convert seconds since the Epoch to a time tuple expressing UTC (a.k.a.
        GMT).  When 'seconds' is not passed in, convert the current time instead.

        If the platform supports the tm_gmtoff and tm_zone, they are available as
        attributes only.
        pass

    :param _float: seconds from since the Epoch
    :return: struct_time
    """
    pass


def _asctime_doc(self, _struct_time):
    """
        asctime(), asctime(sec)
        Convert a tuple or struct_time representing a time
        as returned by gmtime() or localtime() to a string

    :param self, _struct_time:
    :return: _str: Date&Time string format
    """
    pass


def _mktime_doc(_struct_time):
    """
    This is the inverse function of localtime().
    Its argument is the struct_time or full 9-tuple (since the dst flag is needed
    :param _struct_time:
    :return: seconds from since the Epoch to
    """
    pass


"""EXAMPLES"""
date_string = "21 June, 2018 08:22:33"


# strptime(string, format) example
def string_to_date_object(_str):
    print("date_string =", _str)
    print(type(_str))

    print('*' * 120)

    _date_obj = time.strptime(_str, "%d %B, %Y %H:%M:%S")
    print(_date_obj)
    print(type(_date_obj))
    return _date_obj


# example gmtime() -> struct_time
date_object_gmt = time.gmtime()

# example localtime() -> struct_time
date_object_locale = time.localtime()

# example gm_time(seconds)
date_since_epoh_gmt = time.gmtime(38471256)

# example local_time(seconds)
date_since_epoh_locale = time.localtime(854997328)

# example asctime()
struct_time_to_str_asc_1 = time.asctime()

# example asctime(date_struct)
struct_time_to_str_asc_2 = time.asctime(date_since_epoh_locale)

#example mktime
struct_time_to_float_second_mktime = time.mktime(date_since_epoh_locale)
print('end file')
