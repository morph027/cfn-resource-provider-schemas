SCHEMA = {
  "typeName" : "AWS::EC2::VPCGatewayAttachment",
  "description" : "Resource Type definition for AWS::EC2::VPCGatewayAttachment",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ec2-vpc-gateway-attachment.git",
  "additionalProperties" : False,
  "properties" : {
    "AttachmentType" : {
      "type" : "string",
      "description" : "Used to identify if this resource is an Internet Gateway or Vpn Gateway Attachment "
    },
    "InternetGatewayId" : {
      "type" : "string",
      "description" : "The ID of the internet gateway. You must specify either InternetGatewayId or VpnGatewayId, but not both."
    },
    "VpcId" : {
      "type" : "string",
      "description" : "The ID of the VPC."
    },
    "VpnGatewayId" : {
      "type" : "string",
      "description" : "The ID of the virtual private gateway. You must specify either InternetGatewayId or VpnGatewayId, but not both."
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "required" : [ "VpcId" ],
  "createOnlyProperties" : [ "/properties/VpcId" ],
  "readOnlyProperties" : [ "/properties/AttachmentType" ],
  "primaryIdentifier" : [ "/properties/AttachmentType", "/properties/VpcId" ],
  "replacementStrategy" : "delete_then_create",
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:AttachInternetGateway", "ec2:AttachVpnGateway", "ec2:DescribeInternetGateways", "ec2:DescribeVpnGateways" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeInternetGateways", "ec2:DescribeVpnGateways" ]
    },
    "update" : {
      "permissions" : [ "ec2:AttachInternetGateway", "ec2:AttachVpnGateway", "ec2:DetachInternetGateway", "ec2:DetachVpnGateway", "ec2:DescribeInternetGateways", "ec2:DescribeVpnGateways" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DetachInternetGateway", "ec2:DetachVpnGateway", "ec2:DescribeInternetGateways", "ec2:DescribeVpnGateways" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeInternetGateways", "ec2:DescribeVpnGateways" ]
    }
  }
}