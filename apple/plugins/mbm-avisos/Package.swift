// swift-tools-version: 5.9
import PackageDescription

let package = Package(
    name: "MbmAvisos",
    platforms: [.iOS(.v15)],
    products: [
        .library(name: "MbmAvisos", targets: ["MbmAvisosPlugin"])
    ],
    dependencies: [
        .package(url: "https://github.com/ionic-team/capacitor-swift-pm.git", from: "8.0.0"),
        .package(url: "https://github.com/OneSignal/OneSignal-XCFramework", from: "5.2.0")
    ],
    targets: [
        .target(
            name: "MbmAvisosPlugin",
            dependencies: [
                .product(name: "Capacitor", package: "capacitor-swift-pm"),
                .product(name: "OneSignalFramework", package: "OneSignal-XCFramework")
            ],
            path: "ios/Sources/MbmAvisosPlugin")
    ]
)
