SCHEMA = {
  "typeName" : "AWS::EC2::TransitGatewayMulticastGroupSource",
  "description" : "The AWS::EC2::TransitGatewayMulticastGroupSource registers and deregisters members and sources (network interfaces) with the transit gateway multicast group",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-transitgatewaymulticastdomain/aws-ec2-transitgatewaymulticastgroupsource",
  "properties" : {
    "GroupIpAddress" : {
      "description" : "The IP address assigned to the transit gateway multicast group.",
      "type" : "string"
    },
    "TransitGatewayAttachmentId" : {
      "description" : "The ID of the transit gateway attachment.",
      "type" : "string"
    },
    "TransitGatewayMulticastDomainId" : {
      "description" : "The ID of the transit gateway multicast domain.",
      "type" : "string"
    },
    "SubnetId" : {
      "description" : "The ID of the subnet.",
      "type" : "string"
    },
    "ResourceId" : {
      "description" : "The ID of the resource.",
      "type" : "string"
    },
    "ResourceType" : {
      "description" : "The type of resource, for example a VPC attachment.",
      "type" : "string"
    },
    "NetworkInterfaceId" : {
      "description" : "The ID of the transit gateway attachment.",
      "type" : "string"
    },
    "GroupMember" : {
      "description" : "Indicates that the resource is a transit gateway multicast group member.",
      "type" : "boolean"
    },
    "GroupSource" : {
      "description" : "Indicates that the resource is a transit gateway multicast group member.",
      "type" : "boolean"
    },
    "SourceType" : {
      "description" : "The source type.",
      "type" : "string"
    }
  },
  "required" : [ "TransitGatewayMulticastDomainId", "NetworkInterfaceId", "GroupIpAddress" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "additionalProperties" : False,
  "readOnlyProperties" : [ "/properties/SubnetId", "/properties/ResourceId", "/properties/ResourceType", "/properties/GroupSource", "/properties/GroupMember", "/properties/SourceType", "/properties/TransitGatewayAttachmentId" ],
  "createOnlyProperties" : [ "/properties/TransitGatewayMulticastDomainId", "/properties/GroupIpAddress", "/properties/NetworkInterfaceId" ],
  "primaryIdentifier" : [ "/properties/TransitGatewayMulticastDomainId", "/properties/GroupIpAddress", "/properties/NetworkInterfaceId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:RegisterTransitGatewayMulticastGroupSources", "ec2:SearchTransitGatewayMulticastGroups" ]
    },
    "read" : {
      "permissions" : [ "ec2:SearchTransitGatewayMulticastGroups" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DeregisterTransitGatewayMulticastGroupSources", "ec2:SearchTransitGatewayMulticastGroups" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "TransitGatewayMulticastDomainId" : {
            "$ref" : "resource-schema.json#/properties/TransitGatewayMulticastDomainId"
          }
        },
        "required" : [ "TransitGatewayMulticastDomainId" ]
      },
      "permissions" : [ "ec2:SearchTransitGatewayMulticastGroups" ]
    }
  }
}