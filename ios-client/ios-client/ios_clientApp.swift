import SwiftUI

@main
struct ios_clientApp: App {
    init() {
        // Apply initial screen-on preference
        UIApplication.shared.isIdleTimerDisabled = SettingsManager.shared.keepScreenOn
    }
    
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
