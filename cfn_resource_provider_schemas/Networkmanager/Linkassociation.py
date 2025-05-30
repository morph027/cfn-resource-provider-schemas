SCHEMA = {
  "typeName" : "AWS::NetworkManager::LinkAssociation",
  "description" : "The AWS::NetworkManager::LinkAssociation type associates a link to a device. The device and link must be in the same global network and the same site.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-networkmanager.git",
  "properties" : {
    "GlobalNetworkId" : {
      "description" : "The ID of the global network.",
      "type" : "string"
    },
    "DeviceId" : {
      "description" : "The ID of the device",
      "type" : "string"
    },
    "LinkId" : {
      "description" : "The ID of the link",
      "type" : "string"
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "additionalProperties" : False,
  "required" : [ "GlobalNetworkId", "DeviceId", "LinkId" ],
  "primaryIdentifier" : [ "/properties/GlobalNetworkId", "/properties/DeviceId", "/properties/LinkId" ],
  "createOnlyProperties" : [ "/properties/GlobalNetworkId", "/properties/DeviceId", "/properties/LinkId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "networkmanager:GetLinkAssociations", "networkmanager:AssociateLink" ]
    },
    "read" : {
      "permissions" : [ "networkmanager:GetLinkAssociations" ]
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
      "permissions" : [ "networkmanager:GetLinkAssociations" ]
    },
    "delete" : {
      "permissions" : [ "networkmanager:DisassociateLink" ]
    }
  }
}