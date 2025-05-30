SCHEMA = {
  "typeName" : "AWS::RDS::DBSecurityGroupIngress",
  "description" : "Resource Type definition for AWS::RDS::DBSecurityGroupIngress",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "CIDRIP" : {
      "type" : "string"
    },
    "DBSecurityGroupName" : {
      "type" : "string"
    },
    "EC2SecurityGroupId" : {
      "type" : "string"
    },
    "EC2SecurityGroupName" : {
      "type" : "string"
    },
    "EC2SecurityGroupOwnerId" : {
      "type" : "string"
    }
  },
  "required" : [ "DBSecurityGroupName" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}