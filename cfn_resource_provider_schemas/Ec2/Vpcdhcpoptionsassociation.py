SCHEMA = {
  "typeName" : "AWS::EC2::VPCDHCPOptionsAssociation",
  "description" : "Associates a set of DHCP options with a VPC, or associates no DHCP options with the VPC.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ec2.git",
  "properties" : {
    "DhcpOptionsId" : {
      "type" : "string",
      "description" : "The ID of the DHCP options set, or default to associate no DHCP options with the VPC."
    },
    "VpcId" : {
      "type" : "string",
      "description" : "The ID of the VPC."
    }
  },
  "additionalProperties" : False,
  "required" : [ "VpcId", "DhcpOptionsId" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "createOnlyProperties" : [ "/properties/DhcpOptionsId", "/properties/VpcId" ],
  "primaryIdentifier" : [ "/properties/DhcpOptionsId", "/properties/VpcId" ],
  "replacementStrategy" : "delete_then_create",
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:AssociateDhcpOptions" ]
    },
    "update" : {
      "permissions" : [ "ec2:AssociateDhcpOptions" ]
    },
    "delete" : {
      "permissions" : [ "ec2:AssociateDhcpOptions" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeVpcs" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeVpcs" ]
    }
  }
}