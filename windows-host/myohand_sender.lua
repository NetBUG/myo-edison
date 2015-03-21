scriptId = 'com.thalmic.examples.outputeverything'
scriptTitle = "Output Everything"
scriptDetailsUrl = "" -- We don't have this until it's submitted to the Myo Market

function onPoseEdge(pose, edge)
    myo.debug("onPoseEdge: " .. pose .. ", " .. edge)
    -- connecting to Edison
    local host, port = "10.9.46.68", 100
    local socket = require("socket")
    local tcp = assert(socket.tcp())

    tcp:connect(host, port);
    -- sending to Edison
    tcp:send("pose");

    --while true do
--	local s, status, partial = tcp:receive()
--	print(s or partial)
--        if status == "closed" then break end
--    end
    local threebytes = tcp:receive(3)
    tcp:close()
    -- if response eq "1", "2" or "3"

    myo.vibrate("short")
end

function onPeriodic()
end

function onForegroundWindowChange(app, title)
    myo.debug("onForegroundWindowChange: " .. app .. ", " .. title)
    return true
end

function activeAppName()
    return "Output Everything"
end

function onActiveChange(isActive)
    myo.debug("onActiveChange")
end