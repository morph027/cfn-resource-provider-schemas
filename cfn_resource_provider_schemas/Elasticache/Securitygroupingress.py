SCHEMA = {
  "typeName" : "AWS::ElastiCache::SecurityGroupIngress",
  "description" : "Resource Type definition for AWS::ElastiCache::SecurityGroupIngress",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "CacheSecurityGroupName" : {
      "type" : "string"
    },
    "EC2SecurityGroupName" : {
      "type" : "string"
    },
    "EC2SecurityGroupOwnerId" : {
      "type" : "string"
    }
  },
  "required" : [ "EC2SecurityGroupName", "CacheSecurityGroupName" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}