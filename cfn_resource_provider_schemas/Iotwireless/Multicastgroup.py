SCHEMA = {
  "typeName" : "AWS::IoTWireless::MulticastGroup",
  "description" : "Create and manage Multicast groups.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "iotwireless:TagResource", "iotwireless:UntagResource", "iotwireless:ListTagsForResource" ]
  },
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "additionalProperties" : False
    },
    "LoRaWAN" : {
      "type" : "object",
      "properties" : {
        "RfRegion" : {
          "description" : "Multicast group LoRaWAN RF region",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 64
        },
        "DlClass" : {
          "description" : "Multicast group LoRaWAN DL Class",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 64
        },
        "NumberOfDevicesRequested" : {
          "description" : "Multicast group number of devices requested. Returned after successful read.",
          "type" : "integer"
        },
        "NumberOfDevicesInGroup" : {
          "description" : "Multicast group number of devices in group. Returned after successful read.",
          "type" : "integer"
        }
      },
      "additionalProperties" : False,
      "required" : [ "RfRegion", "DlClass" ]
    }
  },
  "properties" : {
    "Name" : {
      "description" : "Name of Multicast group",
      "type" : "string",
      "maxLength" : 256
    },
    "Description" : {
      "description" : "Multicast group description",
      "type" : "string",
      "maxLength" : 2048
    },
    "LoRaWAN" : {
      "description" : "Multicast group LoRaWAN",
      "$ref" : "#/definitions/LoRaWAN"
    },
    "Arn" : {
      "description" : "Multicast group arn. Returned after successful create.",
      "type" : "string"
    },
    "Id" : {
      "description" : "Multicast group id. Returned after successful create.",
      "type" : "string",
      "maxLength" : 256
    },
    "Tags" : {
      "description" : "A list of key-value pairs that contain metadata for the Multicast group.",
      "type" : "array",
      "uniqueItems" : True,
      "maxItems" : 200,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Status" : {
      "description" : "Multicast group status. Returned after successful read.",
      "type" : "string"
    },
    "AssociateWirelessDevice" : {
      "description" : "Wireless device to associate. Only for update request.",
      "type" : "string",
      "maxLength" : 256
    },
    "DisassociateWirelessDevice" : {
      "description" : "Wireless device to disassociate. Only for update request.",
      "type" : "string",
      "maxLength" : 256
    }
  },
  "additionalProperties" : False,
  "required" : [ "LoRaWAN" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Id", "/properties/Status", "/properties/LoRaWAN/NumberOfDevicesRequested", "/properties/LoRaWAN/NumberOfDevicesInGroup" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iotwireless:CreateMulticastGroup", "iotwireless:TagResource" ]
    },
    "read" : {
      "permissions" : [ "iotwireless:GetMulticastGroup", "iotwireless:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "iotwireless:UpdateMulticastGroup", "iotwireless:GetMulticastGroup", "iotwireless:TagResource", "iotwireless:UntagResource", "iotwireless:AssociateWirelessDeviceWithMulticastGroup", "iotwireless:DisassociateWirelessDeviceFromMulticastGroup" ]
    },
    "delete" : {
      "permissions" : [ "iotwireless:DeleteMulticastGroup" ]
    },
    "list" : {
      "permissions" : [ "iotwireless:ListMulticastGroups", "iotwireless:ListTagsForResource" ]
    }
  }
}