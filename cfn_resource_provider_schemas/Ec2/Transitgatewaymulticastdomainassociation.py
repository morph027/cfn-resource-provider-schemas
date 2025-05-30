SCHEMA = {
  "typeName" : "AWS::EC2::TransitGatewayMulticastDomainAssociation",
  "description" : "The AWS::EC2::TransitGatewayMulticastDomainAssociation type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-myservice",
  "properties" : {
    "TransitGatewayMulticastDomainId" : {
      "description" : "The ID of the transit gateway multicast domain.",
      "type" : "string"
    },
    "TransitGatewayAttachmentId" : {
      "description" : "The ID of the transit gateway attachment.",
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
    "State" : {
      "description" : "The state of the subnet association.",
      "type" : "string"
    },
    "SubnetId" : {
      "description" : "The IDs of the subnets to associate with the transit gateway multicast domain.",
      "type" : "string"
    }
  },
  "required" : [ "TransitGatewayMulticastDomainId", "TransitGatewayAttachmentId", "SubnetId" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "additionalProperties" : False,
  "readOnlyProperties" : [ "/properties/ResourceId", "/properties/ResourceType", "/properties/State" ],
  "createOnlyProperties" : [ "/properties/TransitGatewayMulticastDomainId", "/properties/TransitGatewayAttachmentId", "/properties/SubnetId" ],
  "primaryIdentifier" : [ "/properties/TransitGatewayMulticastDomainId", "/properties/TransitGatewayAttachmentId", "/properties/SubnetId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:AssociateTransitGatewayMulticastDomain", "ec2:GetTransitGatewayMulticastDomainAssociations" ]
    },
    "read" : {
      "permissions" : [ "ec2:GetTransitGatewayMulticastDomainAssociations" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DisassociateTransitGatewayMulticastDomain", "ec2:GetTransitGatewayMulticastDomainAssociations" ]
    },
    "list" : {
      "permissions" : [ "ec2:GetTransitGatewayMulticastDomainAssociations" ]
    }
  }
}