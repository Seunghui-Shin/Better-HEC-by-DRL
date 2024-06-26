
from concurrent.futures import Future, TimeoutError
from functools import partial
from deprecated import deprecated
from enum import Enum
from ... import  RouterClient
from ...NotificationHandler import NotificationHandler
from ... import BitMaskTools
from ..messages import Base_pb2 as BasePb  # NOQA


class BaseFunctionUid(Enum):
    uidCreateUserProfile = 0x20001
    uidUpdateUserProfile = 0x20002
    uidReadUserProfile = 0x20003
    uidDeleteUserProfile = 0x20004
    uidReadAllUserProfiles = 0x20005
    uidReadAllUsers = 0x20006
    uidChangePassword = 0x20007
    uidCreateSequence = 0x20008
    uidUpdateSequence = 0x20009
    uidReadSequence = 0x2000a
    uidDeleteSequence = 0x2000b
    uidReadAllSequences = 0x2000c
    uidPlaySequence = 0x2000f
    uidPlayAdvancedSequence = 0x20010
    uidStopSequence = 0x20011
    uidPauseSequence = 0x20012
    uidResumeSequence = 0x20013
    uidCreateProtectionZone = 0x20014
    uidUpdateProtectionZone = 0x20015
    uidReadProtectionZone = 0x20016
    uidDeleteProtectionZone = 0x20017
    uidReadAllProtectionZones = 0x20018
    uidCreateMapping = 0x2001a
    uidReadMapping = 0x2001b
    uidUpdateMapping = 0x2001c
    uidDeleteMapping = 0x2001d
    uidReadAllMappings = 0x2001e
    uidCreateMap = 0x20024
    uidReadMap = 0x20025
    uidUpdateMap = 0x20026
    uidDeleteMap = 0x20027
    uidReadAllMaps = 0x20028
    uidActivateMap = 0x20029
    uidCreateAction = 0x2002a
    uidReadAction = 0x2002b
    uidReadAllActions = 0x2002c
    uidDeleteAction = 0x2002d
    uidUpdateAction = 0x2002e
    uidExecuteActionFromReference = 0x2002f
    uidExecuteAction = 0x20030
    uidPauseAction = 0x20031
    uidStopAction = 0x20032
    uidResumeAction = 0x20033
    uidGetIPv4Configuration = 0x2003b
    uidSetIPv4Configuration = 0x2003c
    uidSetCommunicationInterfaceEnable = 0x2003d
    uidIsCommunicationInterfaceEnable = 0x2003e
    uidGetAvailableWifi = 0x2003f
    uidGetWifiInformation = 0x20040
    uidAddWifiConfiguration = 0x20041
    uidDeleteWifiConfiguration = 0x20042
    uidGetAllConfiguredWifis = 0x20043
    uidConnectWifi = 0x20044
    uidDisconnectWifi = 0x20045
    uidGetConnectedWifiInformation = 0x20046
    uidUnsubscribe = 0x20061
    uidOnNotificationConfigurationChangeTopic = 0x20062
    uidOnNotificationMappingInfoTopic = 0x20063
    uidOnNotificationControlModeTopic = 0x20064
    uidOnNotificationOperatingModeTopic = 0x20065
    uidOnNotificationSequenceInfoTopic = 0x20066
    uidOnNotificationProtectionZoneTopic = 0x20067
    uidOnNotificationUserTopic = 0x20068
    uidOnNotificationControllerTopic = 0x20069
    uidOnNotificationActionTopic = 0x2006a
    uidOnNotificationRobotEventTopic = 0x2006b
    uidPlayCartesianTrajectory = 0x2006d
    uidPlayCartesianTrajectoryPosition = 0x2006e
    uidPlayCartesianTrajectoryOrientation = 0x2006f
    uidStop = 0x20070
    uidGetMeasuredCartesianPose = 0x20073
    uidSendWrenchCommand = 0x20076
    uidSendWrenchJoystickCommand = 0x20077
    uidSendTwistJoystickCommand = 0x20078
    uidSendTwistCommand = 0x20079
    uidPlayJointTrajectory = 0x2007c
    uidPlaySelectedJointTrajectory = 0x2007d
    uidGetMeasuredJointAngles = 0x2007e
    uidSendJointSpeedsCommand = 0x20084
    uidSendSelectedJointSpeedCommand = 0x20085
    uidSendGripperCommand = 0x20088
    uidGetMeasuredGripperMovement = 0x20089
    uidSetAdmittance = 0x2008b
    uidSetOperatingMode = 0x2008d
    uidApplyEmergencyStop = 0x20091
    uidClearFaults = 0x20092
    uidGetControlMode = 0x20096
    uidGetOperatingMode = 0x20097
    uidSetServoingMode = 0x20098
    uidGetServoingMode = 0x20099
    uidOnNotificationServoingModeTopic = 0x2009a
    uidRestoreFactorySettings = 0x200a0
    uidReboot = 0x200a2
    uidOnNotificationFactoryTopic = 0x200a4
    uidGetAllConnectedControllers = 0x200a6
    uidGetControllerState = 0x200a7
    uidGetActuatorCount = 0x200ab
    uidStartWifiScan = 0x200ac
    uidGetConfiguredWifi = 0x200ad
    uidOnNotificationNetworkTopic = 0x200ae
    uidGetArmState = 0x200af
    uidOnNotificationArmStateTopic = 0x200b0
    uidGetIPv4Information = 0x200b1
    uidSetWifiCountryCode = 0x200b2
    uidGetWifiCountryCode = 0x200b3
    uidSetCapSenseConfig = 0x200b4
    uidGetCapSenseConfig = 0x200b5
    uidGetAllJointsSpeedHardLimitation = 0x200b7
    uidGetAllJointsTorqueHardLimitation = 0x200b8
    uidGetTwistHardLimitation = 0x200b9
    uidGetWrenchHardLimitation = 0x200ba
    uidSendJointSpeedsJoystickCommand = 0x200bb
    uidSendSelectedJointSpeedJoystickCommand = 0x200bc
    uidEnableBridge = 0x200c1
    uidDisableBridge = 0x200c2
    uidGetBridgeList = 0x200c3
    uidGetBridgeConfig = 0x200c4
    uidPlayPreComputedJointTrajectory = 0x200c5
    uidGetProductConfiguration = 0x200c6
    uidUpdateEndEffectorTypeConfiguration = 0x200c9
    uidRestoreFactoryProductConfiguration = 0x200ce
    uidGetTrajectoryErrorReport = 0x200cf
    uidGetAllJointsSpeedSoftLimitation = 0x200d0
    uidGetAllJointsTorqueSoftLimitation = 0x200d1
    uidGetTwistSoftLimitation = 0x200d2
    uidGetWrenchSoftLimitation = 0x200d3
    uidSetControllerConfigurationMode = 0x200d4
    uidGetControllerConfigurationMode = 0x200d5
    uidStartTeaching = 0x200d6
    uidStopTeaching = 0x200d7
    uidAddSequenceTasks = 0x200d8
    uidUpdateSequenceTask = 0x200d9
    uidSwapSequenceTasks = 0x200da
    uidReadSequenceTask = 0x200db
    uidReadAllSequenceTasks = 0x200dc
    uidDeleteSequenceTask = 0x2000d
    uidDeleteAllSequenceTasks = 0x2000e
    uidTakeSnapshot = 0x200df
    uidGetFirmwareBundleVersions = 0x200e0
    uidExecuteWaypointTrajectory = 0x200e2
    uidMoveSequenceTask = 0x200e3
    uidDuplicateMapping = 0x200e4
    uidDuplicateMap = 0x200e5
    uidSetControllerConfiguration = 0x200e6
    uidGetControllerConfiguration = 0x200e7
    uidGetAllControllerConfigurations = 0x200e8
    uidComputeForwardKinematics = 0x200e9
    uidComputeInverseKinematics = 0x200ea
    uidValidateWaypointList = 0x200eb
    uidSetWifiEnableState = 0x200ec
    uidGetWifiEnableState = 0x200ed
    uidSetBluetoothEnableState = 0x200ee
    uidGetBluetoothEnableState = 0x200ef



class BaseClient():
    
    serviceVersion = 1
    serviceId = 2
    router = RouterClient.RouterClient

    def __init__(self, router: RouterClient.RouterClient):
        self.router = router
        self.notificationHandler = NotificationHandler()
        callback = partial(self.ExecuteRouterNotification)
        self.router.registerNotificationCallback(self.serviceId, callback)

    def ExecuteRouterNotification(self, message):
        self.notificationHandler.call(BitMaskTools.extractFrameId(message.header.message_info), message.payload)


    def CreateUserProfile(self, fulluserprofile, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = fulluserprofile.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidCreateUserProfile, deviceId, options)

        ansPayload = BasePb.UserProfileHandle()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def UpdateUserProfile(self, userprofile, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = userprofile.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidUpdateUserProfile, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def ReadUserProfile(self, userprofilehandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = userprofilehandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidReadUserProfile, deviceId, options)

        ansPayload = BasePb.UserProfile()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def DeleteUserProfile(self, userprofilehandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = userprofilehandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidDeleteUserProfile, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def ReadAllUserProfiles(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidReadAllUserProfiles, deviceId, options)

        ansPayload = BasePb.UserProfileList()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def ReadAllUsers(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidReadAllUsers, deviceId, options)

        ansPayload = BasePb.UserList()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def ChangePassword(self, passwordchange, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = passwordchange.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidChangePassword, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def CreateSequence(self, sequence, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = sequence.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidCreateSequence, deviceId, options)

        ansPayload = BasePb.SequenceHandle()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def UpdateSequence(self, sequence, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = sequence.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidUpdateSequence, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def ReadSequence(self, sequencehandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = sequencehandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidReadSequence, deviceId, options)

        ansPayload = BasePb.Sequence()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def DeleteSequence(self, sequencehandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = sequencehandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidDeleteSequence, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def ReadAllSequences(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidReadAllSequences, deviceId, options)

        ansPayload = BasePb.SequenceList()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def PlaySequence(self, sequencehandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = sequencehandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidPlaySequence, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def PlayAdvancedSequence(self, advancedsequencehandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = advancedsequencehandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidPlayAdvancedSequence, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def StopSequence(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidStopSequence, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def PauseSequence(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidPauseSequence, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def ResumeSequence(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidResumeSequence, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def CreateProtectionZone(self, protectionzone, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = protectionzone.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidCreateProtectionZone, deviceId, options)

        ansPayload = BasePb.ProtectionZoneHandle()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def UpdateProtectionZone(self, protectionzone, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = protectionzone.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidUpdateProtectionZone, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def ReadProtectionZone(self, protectionzonehandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = protectionzonehandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidReadProtectionZone, deviceId, options)

        ansPayload = BasePb.ProtectionZone()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def DeleteProtectionZone(self, protectionzonehandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = protectionzonehandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidDeleteProtectionZone, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def ReadAllProtectionZones(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidReadAllProtectionZones, deviceId, options)

        ansPayload = BasePb.ProtectionZoneList()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def CreateMapping(self, mapping, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = mapping.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidCreateMapping, deviceId, options)

        ansPayload = BasePb.MappingHandle()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def ReadMapping(self, mappinghandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = mappinghandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidReadMapping, deviceId, options)

        ansPayload = BasePb.Mapping()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def UpdateMapping(self, mapping, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = mapping.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidUpdateMapping, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def DeleteMapping(self, mappinghandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = mappinghandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidDeleteMapping, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def ReadAllMappings(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidReadAllMappings, deviceId, options)

        ansPayload = BasePb.MappingList()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def CreateMap(self, map, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = map.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidCreateMap, deviceId, options)

        ansPayload = BasePb.MapHandle()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def ReadMap(self, maphandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = maphandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidReadMap, deviceId, options)

        ansPayload = BasePb.Map()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def UpdateMap(self, map, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = map.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidUpdateMap, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def DeleteMap(self, maphandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = maphandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidDeleteMap, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def ReadAllMaps(self, mappinghandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = mappinghandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidReadAllMaps, deviceId, options)

        ansPayload = BasePb.MapList()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def ActivateMap(self, activatemaphandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = activatemaphandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidActivateMap, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def CreateAction(self, action, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = action.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidCreateAction, deviceId, options)

        ansPayload = BasePb.ActionHandle()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def ReadAction(self, actionhandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = actionhandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidReadAction, deviceId, options)

        ansPayload = BasePb.Action()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def ReadAllActions(self, requestedactiontype, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = requestedactiontype.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidReadAllActions, deviceId, options)

        ansPayload = BasePb.ActionList()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def DeleteAction(self, actionhandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = actionhandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidDeleteAction, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def UpdateAction(self, action, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = action.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidUpdateAction, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def ExecuteActionFromReference(self, actionhandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = actionhandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidExecuteActionFromReference, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def ExecuteAction(self, action, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = action.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidExecuteAction, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def PauseAction(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidPauseAction, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def StopAction(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidStopAction, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def ResumeAction(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidResumeAction, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def GetIPv4Configuration(self, networkhandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = networkhandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidGetIPv4Configuration, deviceId, options)

        ansPayload = BasePb.IPv4Configuration()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def SetIPv4Configuration(self, fullipv4configuration, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = fullipv4configuration.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidSetIPv4Configuration, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def SetCommunicationInterfaceEnable(self, communicationinterfaceconfiguration, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = communicationinterfaceconfiguration.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidSetCommunicationInterfaceEnable, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def IsCommunicationInterfaceEnable(self, networkhandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = networkhandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidIsCommunicationInterfaceEnable, deviceId, options)

        ansPayload = BasePb.CommunicationInterfaceConfiguration()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def GetAvailableWifi(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetAvailableWifi, deviceId, options)

        ansPayload = BasePb.WifiInformationList()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def GetWifiInformation(self, ssid, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = ssid.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidGetWifiInformation, deviceId, options)

        ansPayload = BasePb.WifiInformation()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def AddWifiConfiguration(self, wificonfiguration, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = wificonfiguration.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidAddWifiConfiguration, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def DeleteWifiConfiguration(self, ssid, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = ssid.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidDeleteWifiConfiguration, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def GetAllConfiguredWifis(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetAllConfiguredWifis, deviceId, options)

        ansPayload = BasePb.WifiConfigurationList()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def ConnectWifi(self, ssid, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = ssid.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidConnectWifi, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def DisconnectWifi(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidDisconnectWifi, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def GetConnectedWifiInformation(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetConnectedWifiInformation, deviceId, options)

        ansPayload = BasePb.WifiInformation()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def Unsubscribe(self, notificationhandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = notificationhandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidUnsubscribe, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def OnNotificationConfigurationChangeTopic(self, callback, notificationoptions, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = notificationoptions.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidOnNotificationConfigurationChangeTopic, deviceId, options)

        ansPayload = BasePb.NotificationHandle()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)

        def parseNotifDataFromString(payload):
            obj = BasePb.ConfigurationChangeNotification()
            obj.ParseFromString(payload)
            return obj

        self.notificationHandler.addCallback(ansPayload.identifier, parseNotifDataFromString, callback)
        return ansPayload

    def OnNotificationMappingInfoTopic(self, callback, notificationoptions, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = notificationoptions.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidOnNotificationMappingInfoTopic, deviceId, options)

        ansPayload = BasePb.NotificationHandle()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)

        def parseNotifDataFromString(payload):
            obj = BasePb.MappingInfoNotification()
            obj.ParseFromString(payload)
            return obj

        self.notificationHandler.addCallback(ansPayload.identifier, parseNotifDataFromString, callback)
        return ansPayload

    @deprecated("This function may be removed in a future release. It has been moved to ControlConfig service.")
    def OnNotificationControlModeTopic(self, callback, notificationoptions, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = notificationoptions.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidOnNotificationControlModeTopic, deviceId, options)

        ansPayload = BasePb.NotificationHandle()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)

        def parseNotifDataFromString(payload):
            obj = BasePb.ControlModeNotification()
            obj.ParseFromString(payload)
            return obj

        self.notificationHandler.addCallback(ansPayload.identifier, parseNotifDataFromString, callback)
        return ansPayload

    def OnNotificationOperatingModeTopic(self, callback, notificationoptions, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = notificationoptions.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidOnNotificationOperatingModeTopic, deviceId, options)

        ansPayload = BasePb.NotificationHandle()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)

        def parseNotifDataFromString(payload):
            obj = BasePb.OperatingModeNotification()
            obj.ParseFromString(payload)
            return obj

        self.notificationHandler.addCallback(ansPayload.identifier, parseNotifDataFromString, callback)
        return ansPayload

    def OnNotificationSequenceInfoTopic(self, callback, notificationoptions, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = notificationoptions.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidOnNotificationSequenceInfoTopic, deviceId, options)

        ansPayload = BasePb.NotificationHandle()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)

        def parseNotifDataFromString(payload):
            obj = BasePb.SequenceInfoNotification()
            obj.ParseFromString(payload)
            return obj

        self.notificationHandler.addCallback(ansPayload.identifier, parseNotifDataFromString, callback)
        return ansPayload

    def OnNotificationProtectionZoneTopic(self, callback, notificationoptions, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = notificationoptions.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidOnNotificationProtectionZoneTopic, deviceId, options)

        ansPayload = BasePb.NotificationHandle()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)

        def parseNotifDataFromString(payload):
            obj = BasePb.ProtectionZoneNotification()
            obj.ParseFromString(payload)
            return obj

        self.notificationHandler.addCallback(ansPayload.identifier, parseNotifDataFromString, callback)
        return ansPayload

    def OnNotificationUserTopic(self, callback, notificationoptions, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = notificationoptions.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidOnNotificationUserTopic, deviceId, options)

        ansPayload = BasePb.NotificationHandle()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)

        def parseNotifDataFromString(payload):
            obj = BasePb.UserNotification()
            obj.ParseFromString(payload)
            return obj

        self.notificationHandler.addCallback(ansPayload.identifier, parseNotifDataFromString, callback)
        return ansPayload

    def OnNotificationControllerTopic(self, callback, notificationoptions, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = notificationoptions.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidOnNotificationControllerTopic, deviceId, options)

        ansPayload = BasePb.NotificationHandle()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)

        def parseNotifDataFromString(payload):
            obj = BasePb.ControllerNotification()
            obj.ParseFromString(payload)
            return obj

        self.notificationHandler.addCallback(ansPayload.identifier, parseNotifDataFromString, callback)
        return ansPayload

    def OnNotificationActionTopic(self, callback, notificationoptions, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = notificationoptions.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidOnNotificationActionTopic, deviceId, options)

        ansPayload = BasePb.NotificationHandle()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)

        def parseNotifDataFromString(payload):
            obj = BasePb.ActionNotification()
            obj.ParseFromString(payload)
            return obj

        self.notificationHandler.addCallback(ansPayload.identifier, parseNotifDataFromString, callback)
        return ansPayload

    def OnNotificationRobotEventTopic(self, callback, notificationoptions, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = notificationoptions.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidOnNotificationRobotEventTopic, deviceId, options)

        ansPayload = BasePb.NotificationHandle()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)

        def parseNotifDataFromString(payload):
            obj = BasePb.RobotEventNotification()
            obj.ParseFromString(payload)
            return obj

        self.notificationHandler.addCallback(ansPayload.identifier, parseNotifDataFromString, callback)
        return ansPayload

    @deprecated
    def PlayCartesianTrajectory(self, constrainedpose, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = constrainedpose.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidPlayCartesianTrajectory, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    @deprecated
    def PlayCartesianTrajectoryPosition(self, constrainedposition, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = constrainedposition.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidPlayCartesianTrajectoryPosition, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    @deprecated
    def PlayCartesianTrajectoryOrientation(self, constrainedorientation, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = constrainedorientation.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidPlayCartesianTrajectoryOrientation, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def Stop(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidStop, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def GetMeasuredCartesianPose(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetMeasuredCartesianPose, deviceId, options)

        ansPayload = BasePb.Pose()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def SendWrenchCommand(self, wrenchcommand, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = wrenchcommand.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidSendWrenchCommand, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def SendWrenchJoystickCommand(self, wrenchcommand, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = wrenchcommand.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidSendWrenchJoystickCommand, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def SendTwistJoystickCommand(self, twistcommand, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = twistcommand.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidSendTwistJoystickCommand, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def SendTwistCommand(self, twistcommand, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = twistcommand.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidSendTwistCommand, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    @deprecated
    def PlayJointTrajectory(self, constrainedjointangles, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = constrainedjointangles.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidPlayJointTrajectory, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    @deprecated
    def PlaySelectedJointTrajectory(self, constrainedjointangle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = constrainedjointangle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidPlaySelectedJointTrajectory, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def GetMeasuredJointAngles(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetMeasuredJointAngles, deviceId, options)

        ansPayload = BasePb.JointAngles()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def SendJointSpeedsCommand(self, jointspeeds, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = jointspeeds.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidSendJointSpeedsCommand, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def SendSelectedJointSpeedCommand(self, jointspeed, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = jointspeed.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidSendSelectedJointSpeedCommand, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def SendGripperCommand(self, grippercommand, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = grippercommand.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidSendGripperCommand, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def GetMeasuredGripperMovement(self, gripperrequest, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = gripperrequest.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidGetMeasuredGripperMovement, deviceId, options)

        ansPayload = BasePb.Gripper()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def SetAdmittance(self, admittance, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = admittance.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidSetAdmittance, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def SetOperatingMode(self, operatingmodeinformation, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = operatingmodeinformation.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidSetOperatingMode, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def ApplyEmergencyStop(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidApplyEmergencyStop, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def ClearFaults(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidClearFaults, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    @deprecated("This function may be removed in a future release. It has been moved to ControlConfig service.")
    def GetControlMode(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetControlMode, deviceId, options)

        ansPayload = BasePb.ControlModeInformation()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def GetOperatingMode(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetOperatingMode, deviceId, options)

        ansPayload = BasePb.OperatingModeInformation()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def SetServoingMode(self, servoingmodeinformation, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = servoingmodeinformation.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidSetServoingMode, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def GetServoingMode(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetServoingMode, deviceId, options)

        ansPayload = BasePb.ServoingModeInformation()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def OnNotificationServoingModeTopic(self, callback, notificationoptions, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = notificationoptions.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidOnNotificationServoingModeTopic, deviceId, options)

        ansPayload = BasePb.NotificationHandle()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)

        def parseNotifDataFromString(payload):
            obj = BasePb.ServoingModeNotification()
            obj.ParseFromString(payload)
            return obj

        self.notificationHandler.addCallback(ansPayload.identifier, parseNotifDataFromString, callback)
        return ansPayload

    def RestoreFactorySettings(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidRestoreFactorySettings, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def Reboot(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidReboot, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def OnNotificationFactoryTopic(self, callback, notificationoptions, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = notificationoptions.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidOnNotificationFactoryTopic, deviceId, options)

        ansPayload = BasePb.NotificationHandle()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)

        def parseNotifDataFromString(payload):
            obj = BasePb.FactoryNotification()
            obj.ParseFromString(payload)
            return obj

        self.notificationHandler.addCallback(ansPayload.identifier, parseNotifDataFromString, callback)
        return ansPayload

    def GetAllConnectedControllers(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetAllConnectedControllers, deviceId, options)

        ansPayload = BasePb.ControllerList()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def GetControllerState(self, controllerhandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = controllerhandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidGetControllerState, deviceId, options)

        ansPayload = BasePb.ControllerState()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def GetActuatorCount(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetActuatorCount, deviceId, options)

        ansPayload = BasePb.ActuatorInformation()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def StartWifiScan(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidStartWifiScan, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def GetConfiguredWifi(self, ssid, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = ssid.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidGetConfiguredWifi, deviceId, options)

        ansPayload = BasePb.WifiConfiguration()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def OnNotificationNetworkTopic(self, callback, notificationoptions, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = notificationoptions.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidOnNotificationNetworkTopic, deviceId, options)

        ansPayload = BasePb.NotificationHandle()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)

        def parseNotifDataFromString(payload):
            obj = BasePb.NetworkNotification()
            obj.ParseFromString(payload)
            return obj

        self.notificationHandler.addCallback(ansPayload.identifier, parseNotifDataFromString, callback)
        return ansPayload

    def GetArmState(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetArmState, deviceId, options)

        ansPayload = BasePb.ArmStateInformation()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def OnNotificationArmStateTopic(self, callback, notificationoptions, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = notificationoptions.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidOnNotificationArmStateTopic, deviceId, options)

        ansPayload = BasePb.NotificationHandle()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)

        def parseNotifDataFromString(payload):
            obj = BasePb.ArmStateNotification()
            obj.ParseFromString(payload)
            return obj

        self.notificationHandler.addCallback(ansPayload.identifier, parseNotifDataFromString, callback)
        return ansPayload

    def GetIPv4Information(self, networkhandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = networkhandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidGetIPv4Information, deviceId, options)

        ansPayload = BasePb.IPv4Information()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def SetWifiCountryCode(self, countrycode, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = countrycode.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidSetWifiCountryCode, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def GetWifiCountryCode(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetWifiCountryCode, deviceId, options)

        ansPayload = BasePb.CountryCode()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def SetCapSenseConfig(self, capsenseconfig, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = capsenseconfig.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidSetCapSenseConfig, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def GetCapSenseConfig(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetCapSenseConfig, deviceId, options)

        ansPayload = BasePb.CapSenseConfig()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    @deprecated("This function will be removed in a future release. Use GetKinematicHardLimits from the ControlConfig service instead.")
    def GetAllJointsSpeedHardLimitation(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetAllJointsSpeedHardLimitation, deviceId, options)

        ansPayload = BasePb.JointsLimitationsList()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    @deprecated
    def GetAllJointsTorqueHardLimitation(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetAllJointsTorqueHardLimitation, deviceId, options)

        ansPayload = BasePb.JointsLimitationsList()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    @deprecated("This function will be removed in a future release. Use GetKinematicHardLimits from the ControlConfig service instead.")
    def GetTwistHardLimitation(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetTwistHardLimitation, deviceId, options)

        ansPayload = BasePb.TwistLimitation()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    @deprecated
    def GetWrenchHardLimitation(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetWrenchHardLimitation, deviceId, options)

        ansPayload = BasePb.WrenchLimitation()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def SendJointSpeedsJoystickCommand(self, jointspeeds, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = jointspeeds.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidSendJointSpeedsJoystickCommand, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def SendSelectedJointSpeedJoystickCommand(self, jointspeed, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = jointspeed.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidSendSelectedJointSpeedJoystickCommand, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def EnableBridge(self, bridgeconfig, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = bridgeconfig.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidEnableBridge, deviceId, options)

        ansPayload = BasePb.BridgeResult()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def DisableBridge(self, bridgeidentifier, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = bridgeidentifier.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidDisableBridge, deviceId, options)

        ansPayload = BasePb.BridgeResult()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def GetBridgeList(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetBridgeList, deviceId, options)

        ansPayload = BasePb.BridgeList()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def GetBridgeConfig(self, bridgeidentifier, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = bridgeidentifier.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidGetBridgeConfig, deviceId, options)

        ansPayload = BasePb.BridgeConfig()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def PlayPreComputedJointTrajectory(self, precomputedjointtrajectory, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = precomputedjointtrajectory.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidPlayPreComputedJointTrajectory, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def GetProductConfiguration(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetProductConfiguration, deviceId, options)

        ansPayload = BasePb.CompleteProductConfiguration()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def UpdateEndEffectorTypeConfiguration(self, productconfigurationendeffectortype, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = productconfigurationendeffectortype.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidUpdateEndEffectorTypeConfiguration, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def RestoreFactoryProductConfiguration(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidRestoreFactoryProductConfiguration, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def GetTrajectoryErrorReport(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetTrajectoryErrorReport, deviceId, options)

        ansPayload = BasePb.TrajectoryErrorReport()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    @deprecated("This function will be removed in a future release. Use GetKinematicSoftLimits from the ControlConfig service instead.")
    def GetAllJointsSpeedSoftLimitation(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetAllJointsSpeedSoftLimitation, deviceId, options)

        ansPayload = BasePb.JointsLimitationsList()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    @deprecated
    def GetAllJointsTorqueSoftLimitation(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetAllJointsTorqueSoftLimitation, deviceId, options)

        ansPayload = BasePb.JointsLimitationsList()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    @deprecated("This function will be removed in a future release. Use GetKinematicSoftLimits from the ControlConfig service instead.")
    def GetTwistSoftLimitation(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetTwistSoftLimitation, deviceId, options)

        ansPayload = BasePb.TwistLimitation()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    @deprecated
    def GetWrenchSoftLimitation(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetWrenchSoftLimitation, deviceId, options)

        ansPayload = BasePb.WrenchLimitation()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def SetControllerConfigurationMode(self, controllerconfigurationmode, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = controllerconfigurationmode.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidSetControllerConfigurationMode, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def GetControllerConfigurationMode(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetControllerConfigurationMode, deviceId, options)

        ansPayload = BasePb.ControllerConfigurationMode()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def StartTeaching(self, sequencetaskhandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = sequencetaskhandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidStartTeaching, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def StopTeaching(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidStopTeaching, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def AddSequenceTasks(self, sequencetasksconfiguration, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = sequencetasksconfiguration.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidAddSequenceTasks, deviceId, options)

        ansPayload = BasePb.SequenceTasksRange()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def UpdateSequenceTask(self, sequencetaskconfiguration, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = sequencetaskconfiguration.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidUpdateSequenceTask, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def SwapSequenceTasks(self, sequencetaskspair, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = sequencetaskspair.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidSwapSequenceTasks, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def ReadSequenceTask(self, sequencetaskhandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = sequencetaskhandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidReadSequenceTask, deviceId, options)

        ansPayload = BasePb.SequenceTask()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def ReadAllSequenceTasks(self, sequencehandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = sequencehandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidReadAllSequenceTasks, deviceId, options)

        ansPayload = BasePb.SequenceTasks()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def DeleteSequenceTask(self, sequencetaskhandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = sequencetaskhandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidDeleteSequenceTask, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def DeleteAllSequenceTasks(self, sequencehandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = sequencehandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidDeleteAllSequenceTasks, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def TakeSnapshot(self, snapshot, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = snapshot.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidTakeSnapshot, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def GetFirmwareBundleVersions(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetFirmwareBundleVersions, deviceId, options)

        ansPayload = BasePb.FirmwareBundleVersions()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def ExecuteWaypointTrajectory(self, waypointlist, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = waypointlist.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidExecuteWaypointTrajectory, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def MoveSequenceTask(self, sequencetaskspair, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = sequencetaskspair.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidMoveSequenceTask, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def DuplicateMapping(self, mappinghandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = mappinghandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidDuplicateMapping, deviceId, options)

        ansPayload = BasePb.MappingHandle()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def DuplicateMap(self, maphandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = maphandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidDuplicateMap, deviceId, options)

        ansPayload = BasePb.MapHandle()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def SetControllerConfiguration(self, controllerconfiguration, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = controllerconfiguration.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidSetControllerConfiguration, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def GetControllerConfiguration(self, controllerhandle, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = controllerhandle.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidGetControllerConfiguration, deviceId, options)

        ansPayload = BasePb.ControllerConfiguration()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def GetAllControllerConfigurations(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetAllControllerConfigurations, deviceId, options)

        ansPayload = BasePb.ControllerConfigurationList()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def ComputeForwardKinematics(self, jointangles, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = jointangles.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidComputeForwardKinematics, deviceId, options)

        ansPayload = BasePb.Pose()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def ComputeInverseKinematics(self, ikdata, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = ikdata.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidComputeInverseKinematics, deviceId, options)

        ansPayload = BasePb.JointAngles()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def ValidateWaypointList(self, waypointlist, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = waypointlist.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidValidateWaypointList, deviceId, options)

        ansPayload = BasePb.WaypointValidationReport()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def SetWifiEnableState(self, wifienablestate, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = wifienablestate.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidSetWifiEnableState, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def GetWifiEnableState(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetWifiEnableState, deviceId, options)

        ansPayload = BasePb.WifiEnableState()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

    def SetBluetoothEnableState(self, bluetoothenablestate, deviceId = 0, options = RouterClient.RouterClientSendOptions()):
        reqPayload = bluetoothenablestate.SerializeToString()

        future = self.router.send(reqPayload, 1, BaseFunctionUid.uidSetBluetoothEnableState, deviceId, options)

        result = future.result(options.getTimeoutInSecond())





    def GetBluetoothEnableState(self, deviceId = 0, options = RouterClient.RouterClientSendOptions()):

        future = self.router.send(None, 1, BaseFunctionUid.uidGetBluetoothEnableState, deviceId, options)

        ansPayload = BasePb.BluetoothEnableState()

        result = future.result(options.getTimeoutInSecond())

        ansPayload.ParseFromString(result.payload)



        return ansPayload

