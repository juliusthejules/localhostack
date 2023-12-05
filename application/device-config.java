import javax.xml.bind.*;

public class DeviceConfiguration {

    private boolean hideIpAddress;
    private boolean hideMacAddress;
    private boolean hideBluetoothAddress;
    private String setHostname;
    private boolean hideAllDeviceInfo;
    private boolean hideAllUserIdentity;

    public boolean isHideIpAddress() {
        return hideIpAddress;
    }

    public void setHideIpAddress(boolean hideIpAddress) {
        this.hideIpAddress = hideIpAddress;
    }

    public boolean isHideMacAddress() {
        return hideMacAddress;
    }

    public void setHideMacAddress(boolean hideMacAddress) {
        this.hideMacAddress = hideMacAddress;
    }

    public boolean isHideBluetoothAddress() {
        return hideBluetoothAddress;
    }

    public void setHideBluetoothAddress(boolean hideBluetoothAddress) {
        this.hideBluetoothAddress = hideBluetoothAddress;
    }

    public String getSetHostname() {
        return setHostname;
    }

    public void setSetHostname(String setHostname) {
        this.setHostname = setHostname;
    }

    public boolean isHideAllDeviceInfo() {
        return hideAllDeviceInfo;
    }

    public void setHideAllDeviceInfo(boolean hideAllDeviceInfo) {
        this.hideAllDeviceInfo = hideAllDeviceInfo;
    }

    public boolean isHideAllUserIdentity() {
        return hideAllUserIdentity;
    }

    public void setHideAllUserIdentity(boolean hideAllUserIdentity) {
        this.hideAllUserIdentity = hideAllUserIdentity;
    }
}
