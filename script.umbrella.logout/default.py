import xbmc
import xbmcgui
import xbmcaddon

ADDON = xbmcaddon.Addon()
ADDON_NAME = ADDON.getAddonInfo('name')


def main():
    options = [
        "Logout Real-Debrid from Umbrella",
        "Logout Trakt from Umbrella",
        "Logout Real-Debrid from ResolveURL",
        "Cancel"
    ]
    
    choice = xbmcgui.Dialog().select(ADDON_NAME, options)
    
    if choice == 3 or choice < 0:
        return

    commands = {
        0: 'RunPlugin(plugin://plugin.video.umbrella/?action=rd_Revoke)',
        1: 'RunPlugin(plugin://plugin.video.umbrella/?action=traktRevoke)',
        2: 'RunPlugin(plugin://script.module.resolveurl/?mode=reset_rd)'
    }

    cmd = commands.get(choice)
    if cmd:
        xbmc.executebuiltin(cmd)
        xbmc.sleep(1000)
        xbmcgui.Dialog().notification(ADDON_NAME, "Logout command sent!", xbmcgui.NOTIFICATION_INFO, 4000)
        xbmc.executebuiltin('Container.Refresh')
    else:
        xbmcgui.Dialog().ok(ADDON_NAME, "Command not found")

if __name__ == "__main__":
    main()