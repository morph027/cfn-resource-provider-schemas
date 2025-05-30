SCHEMA = {
  "typeName" : "AWS::EC2::SubnetNetworkAclAssociation",
  "description" : "Resource Type definition for AWS::EC2::SubnetNetworkAclAssociation",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ec2.git",
  "additionalProperties" : False,
  "properties" : {
    "SubnetId" : {
      "type" : "string",
      "description" : "The ID of the subnet"
    },
    "NetworkAclId" : {
      "type" : "string",
      "description" : "The ID of the network ACL"
    },
    "AssociationId" : {
      "type" : "string"
    }
  },
  "required" : [ "NetworkAclId", "SubnetId" ],
  "replacementStrategy" : "delete_then_create",
  "createOnlyProperties" : [ "/properties/SubnetId", "/properties/NetworkAclId" ],
  "primaryIdentifier" : [ "/properties/AssociationId" ],
  "readOnlyProperties" : [ "/properties/AssociationId" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:DescribeNetworkAcls", "ec2:ReplaceNetworkAclAssociation" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeNetworkAcls" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DescribeNetworkAcls", "ec2:ReplaceNetworkAclAssociation" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeNetworkAcls" ]
    }
  }
}