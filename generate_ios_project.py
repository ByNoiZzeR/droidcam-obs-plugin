import os
import sys

def main():
    print("Generating Xcode project structure for iOS client...")
    
    project_dir = "ios-client"
    xcodeproj_dir = os.path.join(project_dir, "ios-client.xcodeproj")
    shared_data_dir = os.path.join(xcodeproj_dir, "xcshareddata")
    schemes_dir = os.path.join(shared_data_dir, "xcschemes")
    source_dir = os.path.join(project_dir, "ios-client")
    assets_dir = os.path.join(source_dir, "Assets.xcassets")
    appicon_dir = os.path.join(assets_dir, "AppIcon.appiconset")
    
    # Create directories
    for d in [xcodeproj_dir, shared_data_dir, schemes_dir, source_dir, assets_dir, appicon_dir]:
        os.makedirs(d, exist_ok=True)
        print(f"Created directory: {d}")
        
    # Write Assets.xcassets Contents.json
    assets_contents = """{
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}"""
    with open(os.path.join(assets_dir, "Contents.json"), "w") as f:
        f.write(assets_contents)
        
    # Write AppIcon Contents.json
    appicon_contents = """{
  "images" : [
    {
      "idiom" : "iphone",
      "size" : "20x20",
      "scale" : "2x"
    },
    {
      "idiom" : "iphone",
      "size" : "20x20",
      "scale" : "3x"
    },
    {
      "idiom" : "iphone",
      "size" : "29x29",
      "scale" : "2x"
    },
    {
      "idiom" : "iphone",
      "size" : "29x29",
      "scale" : "3x"
    },
    {
      "idiom" : "iphone",
      "size" : "40x40",
      "scale" : "2x"
    },
    {
      "idiom" : "iphone",
      "size" : "40x40",
      "scale" : "3x"
    },
    {
      "idiom" : "iphone",
      "size" : "60x60",
      "scale" : "2x"
    },
    {
      "idiom" : "iphone",
      "size" : "60x60",
      "scale" : "3x"
    },
    {
      "idiom" : "ios-marketing",
      "size" : "1024x1024",
      "scale" : "1x"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}"""
    with open(os.path.join(appicon_dir, "Contents.json"), "w") as f:
        f.write(appicon_contents)
        
    # Write project.pbxproj (with ad-hoc signing allowed)
    pbxproj_content = """// !$*UTF8*$!
{
	archiveVersion = 1;
	classes = {
	};
	objectVersion = 55;
	objects = {

/* Begin PBXBuildFile section */
		9B0101012C12345600123456 /* ios_clientApp.swift in Sources */ = {isa = PBXBuildFile; fileRef = 9B0102012C12345600123456 /* ios_clientApp.swift */; };
		9B0101022C12345600123456 /* ContentView.swift in Sources */ = {isa = PBXBuildFile; fileRef = 9B0102022C12345600123456 /* ContentView.swift */; };
		9B0101032C12345600123456 /* CameraStreamer.swift in Sources */ = {isa = PBXBuildFile; fileRef = 9B0102032C12345600123456 /* CameraStreamer.swift */; };
		9B0101042C12345600123456 /* SocketServer.swift in Sources */ = {isa = PBXBuildFile; fileRef = 9B0102042C12345600123456 /* SocketServer.swift */; };
		9B0101052C12345600123456 /* SettingsManager.swift in Sources */ = {isa = PBXBuildFile; fileRef = 9B0102052C12345600123456 /* SettingsManager.swift */; };
		9B0101062C12345600123456 /* Assets.xcassets in Resources */ = {isa = PBXBuildFile; fileRef = 9B0102062C12345600123456 /* Assets.xcassets */; };
/* End PBXBuildFile section */

/* Begin PBXFileReference section */
		9B0102012C12345600123456 /* ios_clientApp.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ios_clientApp.swift; sourceTree = "<group>"; };
		9B0102022C12345600123456 /* ContentView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ContentView.swift; sourceTree = "<group>"; };
		9B0102032C12345600123456 /* CameraStreamer.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = CameraStreamer.swift; sourceTree = "<group>"; };
		9B0102042C12345600123456 /* SocketServer.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SocketServer.swift; sourceTree = "<group>"; };
		9B0102052C12345600123456 /* SettingsManager.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SettingsManager.swift; sourceTree = "<group>"; };
		9B0102062C12345600123456 /* Assets.xcassets */ = {isa = PBXFileReference; lastKnownFileType = folder.assetcatalog; path = Assets.xcassets; sourceTree = "<group>"; };
		9B0102072C12345600123456 /* Info.plist */ = {isa = PBXFileReference; lastKnownFileType = text.plist.xml; path = Info.plist; sourceTree = "<group>"; };
/* End PBXFileReference section */

/* Begin PBXFrameworksBuildPhase section */
		9B0103012C12345600123456 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
		9B0104012C12345600123456 /* CustomGroup */ = {
			isa = PBXGroup;
			children = (
				9B0104022C12345600123456 /* ios-client */,
				9B0104032C12345600123456 /* Products */,
			);
			sourceTree = "<group>";
		};
		9B0104022C12345600123456 /* ios-client */ = {
			isa = PBXGroup;
			children = (
				9B0102012C12345600123456 /* ios_clientApp.swift */,
				9B0102022C12345600123456 /* ContentView.swift */,
				9B0102032C12345600123456 /* CameraStreamer.swift */,
				9B0102042C12345600123456 /* SocketServer.swift */,
				9B0102052C12345600123456 /* SettingsManager.swift */,
				9B0102062C12345600123456 /* Assets.xcassets */,
				9B0102072C12345600123456 /* Info.plist */,
			);
			path = "ios-client";
			sourceTree = "<group>";
		};
		9B0104032C12345600123456 /* Products */ = {
			isa = PBXGroup;
			children = (
				9B0105012C12345600123456 /* ios-client.app */,
			);
			name = Products;
			sourceTree = "<group>";
		};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
		9B0106012C12345600123456 /* ios-client */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = 9B0107012C12345600123456 /* Build configuration list for PBXNativeTarget "ios-client" */;
			buildPhases = (
				9B0108012C12345600123456 /* Sources */,
				9B0103012C12345600123456 /* Frameworks */,
				9B0109012C12345600123456 /* Resources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = "ios-client";
			productName = "ios-client";
			productReference = 9B0105012C12345600123456 /* ios-client.app */;
			productType = "com.apple.product-type.application";
		};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
		9B010A012C12345600123456 /* Project object */ = {
			isa = PBXProject;
			attributes = {
				BuildIndependentTargetsInParallel = 1;
				LastSwiftUpdateCheck = 1300;
				LastUpgradeCheck = 1300;
				TargetAttributes = {
					9B0106012C12345600123456 = {
						CreatedOnToolsVersion = 13.0;
						DevelopmentTeam = "";
						LastSwiftMigration = 1300;
					};
				};
			};
			buildConfigurationList = 9B010B012C12345600123456 /* Build configuration list for PBXProject "ios-client" */;
			compatibilityVersion = "Xcode 13.0";
			developmentRegion = en;
			hasScannedForEncodings = 0;
			knownRegions = (
				en,
				Base,
			);
			mainGroup = 9B0104012C12345600123456 /* CustomGroup */;
			productRefGroup = 9B0104032C12345600123456 /* Products */;
			projectDirPath = "";
			projectRoot = "";
			targets = (
				9B0106012C12345600123456 /* ios-client */,
			);
		};
/* End PBXProject section */

/* Begin PBXResourcesBuildPhase section */
		9B0109012C12345600123456 /* Resources */ = {
			isa = PBXResourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				9B0101062C12345600123456 /* Assets.xcassets in Resources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXResourcesBuildPhase section */

/* Begin PBXSourcesBuildPhase section */
		9B0108012C12345600123456 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				9B0101012C12345600123456 /* ios_clientApp.swift in Sources */,
				9B0101022C12345600123456 /* ContentView.swift in Sources */,
				9B0101032C12345600123456 /* CameraStreamer.swift in Sources */,
				9B0101042C12345600123456 /* SocketServer.swift in Sources */,
				9B0101052C12345600123456 /* SettingsManager.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXSourcesBuildPhase section */

/* Begin XCBuildConfiguration section */
		9B010C012C12345600123456 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++17";
				CLANG_CXX_LIBRARY = "libc++";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_ENABLE_OBJC_WEAK = YES;
				CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_COMMA = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
				CLANG_WARN_DIRECT_OBJC_REPLAY = YES;
				CLANG_WARN_DOCUMENTATION_COMMENTS = YES;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INFINITE_RECURSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
				CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES;
				CLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
				CLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
				CLANG_WARN_QUOTED_INCLUDE_IN_FRAMEWORK_HEADER = YES;
				CLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
				CLANG_WARN_STRICT_PROTOTYPES = YES;
				CLANG_WARN_SUSPICIOUS_MOVE = YES;
				CLANG_WARN_UNGUARDED_AVAILABILITY = YES_AGGRESSIVE;
				CLANG_WARN_UNREACHABLE_CODE = YES;
				CLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = dwarf;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				ENABLE_TESTABILITY = YES;
				GCC_C_LANGUAGE_STANDARD = gnu11;
				GCC_DYNAMIC_NO_PIC = NO;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_OPTIMIZATION_LEVEL = 0;
				GCC_PREPROCESSOR_DEFINITIONS = (
					"DEBUG=1",
					"$(inherited)",
				);
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNDECLARED_SELECTOR = YES;
				GCC_WARN_UNINITIALIZED_ACTUAL = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				IPHONEOS_DEPLOYMENT_TARGET = 15.0;
				MTL_ENABLE_DEBUG_INFO = INCLUDE_SOURCE;
				MTL_FAST_MATH = YES;
				ONLY_ACTIVE_ARCH = YES;
				SDKROOT = iphoneos;
				SWIFT_ACTIVE_COMPILATION_CONDITIONS = DEBUG;
				SWIFT_OPTIMIZATION_LEVEL = "-Onone";
			};
			name = Debug;
		};
		9B010C022C12345600123456 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++17";
				CLANG_CXX_LIBRARY = "libc++";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_ENABLE_OBJC_WEAK = YES;
				CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_COMMA = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
				CLANG_WARN_DIRECT_OBJC_REPLAY = YES;
				CLANG_WARN_DOCUMENTATION_COMMENTS = YES;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INFINITE_RECURSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
				CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES;
				CLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
				CLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
				CLANG_WARN_QUOTED_INCLUDE_IN_FRAMEWORK_HEADER = YES;
				CLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
				CLANG_WARN_STRICT_PROTOTYPES = YES;
				CLANG_WARN_SUSPICIOUS_MOVE = YES;
				CLANG_WARN_UNGUARDED_AVAILABILITY = YES_AGGRESSIVE;
				CLANG_WARN_UNREACHABLE_CODE = YES;
				CLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
				ENABLE_NS_ASSERTIONS = NO;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				GCC_C_LANGUAGE_STANDARD = gnu11;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNDECLARED_SELECTOR = YES;
				GCC_WARN_UNINITIALIZED_ACTUAL = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				IPHONEOS_DEPLOYMENT_TARGET = 15.0;
				MTL_ENABLE_DEBUG_INFO = NO;
				MTL_FAST_MATH = YES;
				SDKROOT = iphoneos;
				SWIFT_COMPILATION_MODE = wholemodule;
				SWIFT_OPTIMIZATION_LEVEL = "-O";
				VALIDATE_PRODUCT = YES;
			};
			name = Release;
		};
		9B010D012C12345600123456 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				ASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
				CODE_SIGN_STYLE = Manual;
				CODE_SIGN_IDENTITY = "-";
				CODE_SIGNING_ALLOWED = YES;
				CODE_SIGNING_REQUIRED = NO;
				INFOPLIST_FILE = "ios-client/Info.plist";
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				PRODUCT_BUNDLE_IDENTIFIER = "com.webcamclone.ios-client";
				PRODUCT_NAME = "$(TARGET_NAME)";
				SWIFT_EMIT_LOC_STRINGS = YES;
				SWIFT_VERSION = 5.0;
				TARGETED_DEVICE_FAMILY = "1,2";
			};
			name = Debug;
		};
		9B010D022C12345600123456 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				ASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
				CODE_SIGN_STYLE = Manual;
				CODE_SIGN_IDENTITY = "-";
				CODE_SIGNING_ALLOWED = YES;
				CODE_SIGNING_REQUIRED = NO;
				INFOPLIST_FILE = "ios-client/Info.plist";
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				PRODUCT_BUNDLE_IDENTIFIER = "com.webcamclone.ios-client";
				PRODUCT_NAME = "$(TARGET_NAME)";
				SWIFT_EMIT_LOC_STRINGS = YES;
				SWIFT_VERSION = 5.0;
				TARGETED_DEVICE_FAMILY = "1,2";
			};
			name = Release;
		};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
		9B0107012C12345600123456 /* Build configuration list for PBXNativeTarget "ios-client" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				9B010D012C12345600123456 /* Debug */,
				9B010D022C12345600123456 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
		9B010B012C12345600123456 /* Build configuration list for PBXProject "ios-client" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				9B010C012C12345600123456 /* Debug */,
				9B010C022C12345600123456 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
/* End XCConfigurationList section */
	};
	rootObject = 9B010A012C12345600123456 /* Project object */;
}
"""
    
    with open(os.path.join(xcodeproj_dir, "project.pbxproj"), "w") as f:
        f.write(pbxproj_content)
        print(f"Generated project.pbxproj file at: {os.path.join(xcodeproj_dir, 'project.pbxproj')}")

    # Write ios-client.xcscheme shared scheme configuration
    scheme_content = """<?xml version="1.0" encoding="UTF-8"?>
<Scheme
   LastUpgradeVersion = "1300"
   version = "1.3">
   <BuildAction
      parallelizeBuildables = "YES"
      buildImplicitDependencies = "YES">
      <BuildActionEntries>
         <BuildActionEntry
            buildForTesting = "YES"
            buildForRunning = "YES"
            buildForProfiling = "YES"
            buildForArchiving = "YES"
            buildForAnalyzing = "YES">
            <BuildableReference
               BuildableIdentifier = "primary"
               BlueprintIdentifier = "9B0106012C12345600123456"
               BuildableName = "ios-client.app"
               BlueprintName = "ios-client"
               ReferencedContainer = "container:ios-client.xcodeproj">
            </BuildableReference>
         </BuildActionEntry>
      </BuildActionEntries>
   </BuildAction>
   <LaunchAction
      buildConfiguration = "Release"
      selectedDebuggerIdentifier = "Xcode.DebuggerFoundation.Debugger.LLDB"
      selectedLauncherIdentifier = "Xcode.DebuggerFoundation.Launcher.LLDB"
      launchStyle = "0"
      useCustomWorkingDirectory = "NO"
      ignoresPersistentStateOnLaunch = "NO"
      debugDocumentVersioning = "YES"
      debugServiceExtension = "internal"
      allowLocationSimulation = "YES">
      <BuildableProductRunnable
         runnableDebuggingMode = "0">
         <BuildableReference
            BuildableIdentifier = "primary"
            BlueprintIdentifier = "9B0106012C12345600123456"
            BuildableName = "ios-client.app"
            BlueprintName = "ios-client"
            ReferencedContainer = "container:ios-client.xcodeproj">
         </BuildableReference>
      </BuildableProductRunnable>
   </LaunchAction>
</Scheme>
"""
    with open(os.path.join(schemes_dir, "ios-client.xcscheme"), "w") as f:
        f.write(scheme_content)
        print(f"Generated shared scheme at: {os.path.join(schemes_dir, 'ios-client.xcscheme')}")

    # Write a dummy product file reference (required by some xcode builders for file indexing)
    product_app = os.path.join(xcodeproj_dir, "ios-client.app")
    with open(product_app, "w") as f:
        f.write("") # empty file placeholder
        
    print("Project successfully generated!")

if __name__ == "__main__":
    main()
