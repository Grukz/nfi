'''
NFI -- Silensec's Nyuki Forensics Investigator

Copyright (C) 2014  George Nicolaou (george[at]silensec[dot]com)
                    Silensec Ltd.
                    
                    Juma Fredrick (j.fredrick[at]silensec[dot]com)
                    Silensec Ltd.

This file is part of Nyuki Forensics Investigator (NFI).

NFI is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

NFI is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with NFI.  If not, see <http://www.gnu.org/licenses/>.
'''
from IApp import IApp, KnownTable, DataTypes
import ConvertUtils

class com_android_email(IApp):
    name = "com.android.email"
    cname = "Android Email"
    databases = {
        "EmailProviderBackup.db": [
            KnownTable("Mailbox", None,
                {"syncTime":ConvertUtils.JsToUnix,
                 "lastTouchedTime":ConvertUtils.JsToUnix},
                {"syncTime":DataTypes.DATE, "lastTouchedTime":DataTypes.DATE}),
            KnownTable("Message", None,
                {"syncServerTimeStamp":ConvertUtils.UnixTimestamp,
                 "timeStamp":ConvertUtils.UnixTimestamp},
                {"syncServerTimeStamp": DataTypes.DATE, 
                 "timeStamp": DataTypes.DATE}),
            KnownTable("Message_Deletes", None,
                {"syncServerTimeStamp":ConvertUtils.UnixTimestamp,
                 "timeStamp":ConvertUtils.UnixTimestamp},
                {"syncServerTimeStamp":DataTypes.DATE, 
                 "timeStamp":DataTypes.DATE}),
            KnownTable("Message_Updates", None,
                {"syncServerTimeStamp":ConvertUtils.UnixTimestamp,
                 "timeStamp":ConvertUtils.UnixTimestamp},
                {"syncServerTimeStamp":DataTypes.DATE, 
                 "timeStamp":DataTypes.DATE}),
        ],
        "EmailProvider.db": [
            KnownTable("Mailbox", None,
                {"syncTime":ConvertUtils.JsToUnix,
                 "lastTouchedTime":ConvertUtils.JsToUnix},
                {"syncTime":DataTypes.DATE, "lastTouchedTime":DataTypes.DATE}),
            KnownTable("Message", None,
                {"syncServerTimeStamp":ConvertUtils.UnixTimestamp,
                 "timeStamp":ConvertUtils.UnixTimestamp},
                {"syncServerTimeStamp": DataTypes.DATE, 
                 "timeStamp": DataTypes.DATE}),
            KnownTable("Message_Deletes", None,
                {"syncServerTimeStamp":ConvertUtils.UnixTimestamp,
                 "timeStamp":ConvertUtils.UnixTimestamp},
                {"syncServerTimeStamp":DataTypes.DATE, 
                 "timeStamp":DataTypes.DATE}),
            KnownTable("Message_Updates", None,
                {"syncServerTimeStamp":ConvertUtils.UnixTimestamp,
                 "timeStamp":ConvertUtils.UnixTimestamp},
                {"syncServerTimeStamp":DataTypes.DATE, 
                 "timeStamp":DataTypes.DATE}),
        ],
    }

    def __init__(self):
        self.known = True
        
