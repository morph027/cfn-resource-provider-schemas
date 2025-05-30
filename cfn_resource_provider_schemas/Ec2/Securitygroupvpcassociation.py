SCHEMA = {
  "typeName" : "AWS::EC2::SecurityGroupVpcAssociation",
  "description" : "Resource type definition for the AWS::EC2::SecurityGroupVpcAssociation resource",
  "definitions" : {
    "SecurityGroupVpcAssociationState" : {
      "type" : "string",
      "additionalProperties" : False,
      "enum" : [ "associating", "associated", "association-failed", "disassociating", "disassociated", "disassociation-failed" ]
    }
  },
  "properties" : {
    "GroupId" : {
      "description" : "The group ID of the specified security group.",
      "type" : "string"
    },
    "VpcId" : {
      "description" : "The ID of the VPC in the security group vpc association.",
      "type" : "string"
    },
    "VpcOwnerId" : {
      "description" : "The owner of the VPC in the security group vpc association.",
      "type" : "string"
    },
    "State" : {
      "description" : "The state of the security group vpc association.",
      "$ref" : "#/definitions/SecurityGroupVpcAssociationState"
    },
    "StateReason" : {
      "description" : "The reason for the state of the security group vpc association.",
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : False
  },
  "required" : [ "GroupId", "VpcId" ],
  "createOnlyProperties" : [ "/properties/GroupId", "/properties/VpcId" ],
  "readOnlyProperties" : [ "/properties/VpcOwnerId", "/properties/State", "/properties/StateReason" ],
  "primaryIdentifier" : [ "/properties/GroupId", "/properties/VpcId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:AssociateSecurityGroupVpc", "ec2:DescribeSecurityGroupVpcAssociations" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeSecurityGroupVpcAssociations" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DisassociateSecurityGroupVpc", "ec2:DescribeSecurityGroupVpcAssociations" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeSecurityGroupVpcAssociations" ]
    }
  }
}