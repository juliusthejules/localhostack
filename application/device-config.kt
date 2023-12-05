import javax.xml.bind.annotation.XmlAccessType
import javax.xml.bind.annotation.XmlAccessorType
import javax.xml.bind.annotation.XmlRootElement

@XmlAccessorType(XmlAccessType.FIELD)
@XmlRootElement(name = "deviceConfiguration")
data class DeviceConfiguration(
    var hideIpAddress: Boolean = false,
    var hideMacAddress: Boolean = false,
    var hideBluetoothAddress: Boolean = false,
    var setHostname: String? = null,
    var hideAllDeviceInfo: Boolean = false,
    var hideAllUserIdentity: Boolean = false
)