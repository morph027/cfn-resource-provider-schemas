SCHEMA = {
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "typeName" : "AWS::EC2::TransitGatewayRouteTableAssociation",
  "description" : "Resource Type definition for AWS::EC2::TransitGatewayRouteTableAssociation",
  "createOnlyProperties" : [ "/properties/TransitGatewayRouteTableId", "/properties/TransitGatewayAttachmentId" ],
  "primaryIdentifier" : [ "/properties/TransitGatewayRouteTableId", "/properties/TransitGatewayAttachmentId" ],
  "required" : [ "TransitGatewayRouteTableId", "TransitGatewayAttachmentId" ],
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-transitgateway.git",
  "handlers" : {
    "read" : {
      "permissions" : [ "ec2:GetTransitGatewayRouteTableAssociations" ]
    },
    "create" : {
      "permissions" : [ "ec2:AssociateTransitGatewayRouteTable", "ec2:GetTransitGatewayRouteTableAssociations" ]
    },
    "list" : {
      "permissions" : [ "ec2:GetTransitGatewayRouteTableAssociations" ],
      "handlerSchema" : {
        "properties" : {
          "TransitGatewayRouteTableId" : {
            "$ref" : "resource-schema.json#/properties/TransitGatewayRouteTableId"
          }
        },
        "required" : [ "TransitGatewayRouteTableId" ]
      }
    },
    "delete" : {
      "permissions" : [ "ec2:GetTransitGatewayRouteTableAssociations", "ec2:DisassociateTransitGatewayRouteTable" ]
    }
  },
  "additionalProperties" : False,
  "definitions" : { },
  "properties" : {
    "TransitGatewayRouteTableId" : {
      "description" : "The ID of transit gateway route table.",
      "type" : "string"
    },
    "TransitGatewayAttachmentId" : {
      "description" : "The ID of transit gateway attachment.",
      "type" : "string"
    }
  },
  "replacementStrategy" : "delete_then_create"
}