SCHEMA = {
  "typeName" : "AWS::Redshift::ClusterSecurityGroupIngress",
  "description" : "Resource Type definition for AWS::Redshift::ClusterSecurityGroupIngress",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "CIDRIP" : {
      "type" : "string"
    },
    "ClusterSecurityGroupName" : {
      "type" : "string"
    },
    "EC2SecurityGroupName" : {
      "type" : "string"
    },
    "EC2SecurityGroupOwnerId" : {
      "type" : "string"
    }
  },
  "required" : [ "ClusterSecurityGroupName" ],
  "createOnlyProperties" : [ "/properties/ClusterSecurityGroupName", "/properties/CIDRIP", "/properties/EC2SecurityGroupOwnerId", "/properties/EC2SecurityGroupName" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}