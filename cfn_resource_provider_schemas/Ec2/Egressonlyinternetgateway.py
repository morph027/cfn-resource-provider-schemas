SCHEMA = {
  "typeName" : "AWS::EC2::EgressOnlyInternetGateway",
  "description" : "Resource Type definition for AWS::EC2::EgressOnlyInternetGateway",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ec2",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "description" : "Service Generated ID of the EgressOnlyInternetGateway",
      "type" : "string"
    },
    "VpcId" : {
      "description" : "The ID of the VPC for which to create the egress-only internet gateway.",
      "type" : "string"
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
  "readOnlyProperties" : [ "/properties/Id" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:CreateEgressOnlyInternetGateway", "ec2:DescribeEgressOnlyInternetGateways" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeEgressOnlyInternetGateways" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DeleteEgressOnlyInternetGateway", "ec2:DescribeEgressOnlyInternetGateways", "ec2:DescribeVpcs" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeEgressOnlyInternetGateways" ]
    }
  }
}