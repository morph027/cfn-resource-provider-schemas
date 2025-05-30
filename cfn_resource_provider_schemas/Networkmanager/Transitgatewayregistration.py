SCHEMA = {
  "typeName" : "AWS::NetworkManager::TransitGatewayRegistration",
  "description" : "The AWS::NetworkManager::TransitGatewayRegistration type registers a transit gateway in your global network. The transit gateway can be in any AWS Region, but it must be owned by the same AWS account that owns the global network. You cannot register a transit gateway in more than one global network.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-networkmanager.git",
  "properties" : {
    "GlobalNetworkId" : {
      "description" : "The ID of the global network.",
      "type" : "string"
    },
    "TransitGatewayArn" : {
      "description" : "The Amazon Resource Name (ARN) of the transit gateway.",
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
  "required" : [ "GlobalNetworkId", "TransitGatewayArn" ],
  "createOnlyProperties" : [ "/properties/GlobalNetworkId", "/properties/TransitGatewayArn" ],
  "primaryIdentifier" : [ "/properties/GlobalNetworkId", "/properties/TransitGatewayArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "networkmanager:RegisterTransitGateway", "networkmanager:GetTransitGatewayRegistrations" ],
      "timeoutInMinutes" : 30
    },
    "read" : {
      "permissions" : [ "networkmanager:GetTransitGatewayRegistrations" ]
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
      "permissions" : [ "networkmanager:GetTransitGatewayRegistrations" ]
    },
    "delete" : {
      "permissions" : [ "networkmanager:DeregisterTransitGateway", "networkmanager:GetTransitGatewayRegistrations" ],
      "timeoutInMinutes" : 30
    }
  }
}