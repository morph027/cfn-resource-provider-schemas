SCHEMA = {
  "typeName" : "AWS::NetworkManager::CustomerGatewayAssociation",
  "description" : "The AWS::NetworkManager::CustomerGatewayAssociation type associates a customer gateway with a device and optionally, with a link.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-networkmanager.git",
  "properties" : {
    "GlobalNetworkId" : {
      "description" : "The ID of the global network.",
      "type" : "string"
    },
    "CustomerGatewayArn" : {
      "description" : "The Amazon Resource Name (ARN) of the customer gateway.",
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
  "required" : [ "GlobalNetworkId", "CustomerGatewayArn", "DeviceId" ],
  "createOnlyProperties" : [ "/properties/GlobalNetworkId", "/properties/CustomerGatewayArn", "/properties/DeviceId", "/properties/LinkId" ],
  "primaryIdentifier" : [ "/properties/GlobalNetworkId", "/properties/CustomerGatewayArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "networkmanager:GetCustomerGatewayAssociations", "networkmanager:AssociateCustomerGateway" ]
    },
    "read" : {
      "permissions" : [ "networkmanager:GetCustomerGatewayAssociations" ]
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
      "permissions" : [ "networkmanager:GetCustomerGatewayAssociations" ]
    },
    "delete" : {
      "permissions" : [ "networkmanager:DisassociateCustomerGateway" ]
    }
  }
}