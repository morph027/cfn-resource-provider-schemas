SCHEMA = {
  "typeName" : "AWS::NetworkManager::Device",
  "description" : "The AWS::NetworkManager::Device type describes a device.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-networkmanager.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a device resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -."
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -."
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "Location" : {
      "description" : "The site location.",
      "type" : "object",
      "properties" : {
        "Address" : {
          "description" : "The physical address.",
          "type" : "string"
        },
        "Latitude" : {
          "description" : "The latitude.",
          "type" : "string"
        },
        "Longitude" : {
          "description" : "The longitude.",
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "AWSLocation" : {
      "description" : "The Amazon Web Services location of the device, if applicable.",
      "type" : "object",
      "properties" : {
        "Zone" : {
          "description" : "The Zone that the device is located in. Specify the ID of an Availability Zone, Local Zone, Wavelength Zone, or an Outpost.",
          "type" : "string"
        },
        "SubnetArn" : {
          "description" : "The Amazon Resource Name (ARN) of the subnet that the device is located in.",
          "type" : "string"
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "DeviceArn" : {
      "description" : "The Amazon Resource Name (ARN) of the device.",
      "type" : "string"
    },
    "DeviceId" : {
      "description" : "The ID of the device.",
      "type" : "string"
    },
    "Description" : {
      "description" : "The description of the device.",
      "type" : "string"
    },
    "Tags" : {
      "description" : "The tags for the device.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "GlobalNetworkId" : {
      "description" : "The ID of the global network.",
      "type" : "string"
    },
    "AWSLocation" : {
      "description" : "The Amazon Web Services location of the device, if applicable.",
      "$ref" : "#/definitions/AWSLocation"
    },
    "Location" : {
      "description" : "The site location.",
      "$ref" : "#/definitions/Location"
    },
    "Model" : {
      "description" : "The device model",
      "type" : "string"
    },
    "SerialNumber" : {
      "description" : "The device serial number.",
      "type" : "string"
    },
    "SiteId" : {
      "description" : "The site ID.",
      "type" : "string"
    },
    "Type" : {
      "description" : "The device type.",
      "type" : "string"
    },
    "Vendor" : {
      "description" : "The device vendor.",
      "type" : "string"
    },
    "CreatedAt" : {
      "description" : "The date and time that the device was created.",
      "type" : "string"
    },
    "State" : {
      "description" : "The state of the device.",
      "type" : "string"
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "networkmanager:TagResource", "networkmanager:UntagResource", "networkmanager:ListTagsForResource" ]
  },
  "additionalProperties" : False,
  "required" : [ "GlobalNetworkId" ],
  "readOnlyProperties" : [ "/properties/DeviceId", "/properties/DeviceArn", "/properties/State", "/properties/CreatedAt" ],
  "createOnlyProperties" : [ "/properties/GlobalNetworkId" ],
  "primaryIdentifier" : [ "/properties/GlobalNetworkId", "/properties/DeviceId" ],
  "additionalIdentifiers" : [ [ "/properties/DeviceArn" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "networkmanager:CreateDevice", "networkmanager:GetDevices", "networkmanager:TagResource" ]
    },
    "read" : {
      "permissions" : [ "networkmanager:GetDevices" ]
    },
    "update" : {
      "permissions" : [ "networkmanager:UpdateDevice", "networkmanager:ListTagsForResource", "networkmanager:GetDevices", "networkmanager:TagResource", "networkmanager:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "networkmanager:GetDevices", "networkmanager:DeleteDevice" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "GlobalNetworkId" : {
            "$ref" : "resource-schema.json#/properties/GlobalNetworkId"
          }
        },
        "required" : [ "GlobalNetworkId" ]
      },
      "permissions" : [ "networkmanager:GetDevices" ]
    }
  }
}